import atexit
import copy
import json
import logging
import os
import pickle
import threading
import time
from typing import Dict

from localstack.utils import files
from localstack.utils.analytics import get_session_id
from localstack.utils.json import CustomEncoder

LOG = logging.getLogger(__name__)

TARGET_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), "../../target"))
REQUESTS_PATH = os.path.join(TARGET_PATH, "api-requests")
RESPONSES_PATH = os.path.join(TARGET_PATH, "api-responses")


def _skel(value):
    if isinstance(value, dict):
        return tuple([(k, _skel(v)) for k, v in value.items()])
    else:
        return str(type(value))


def get_skeleton(api_request):
    return (
        api_request["service"],
        api_request["operation"],
        _skel(api_request["params"]),
    )


class ApiRequestRecorder:
    def __init__(self, dirpath=None) -> None:
        self.dirpath = dirpath or REQUESTS_PATH
        self.last_event = None
        self.skeletons = set()
        self.calls = list()
        self.mutex = threading.RLock()
        atexit.register(self.flush)

    def record(self, service: str, operation: str, request: Dict):
        try:
            payload = {"service": service, "operation": operation, "params": request}

            skeleton = get_skeleton(payload)
            if skeleton in self.skeletons:
                return
            self.skeletons.add(skeleton)

            if len(str(payload)) > 100000:
                # skip request payloads above 100kb
                return

            with self.mutex:
                self.calls.append(payload)
                if len(self.calls) > 50:
                    self.flush()

        except Exception:
            LOG.exception("error while recording API calls")

    def flush(self):
        with self.mutex:
            if not self.calls:
                return
            try:
                f = f"calls-{get_session_id()}.ndjson"
                files.mkdir(self.dirpath)

                with open(os.path.join(self.dirpath, f), "a") as fd:
                    while self.calls:
                        try:
                            call = self.calls.pop()
                            doc = json.dumps(call, cls=CustomEncoder)
                            fd.write(doc)
                            fd.write("\n")
                        except Exception:
                            LOG.exception("error while pickling API call")

            except Exception:
                LOG.exception("error while pickling API calls")


class ApiResponseRecorder:
    def __init__(self, dirpath=None) -> None:
        self.dirpath = dirpath or RESPONSES_PATH
        self.last_event = None
        self.skeletons = set()
        self.calls = list()
        self.records = list()
        self.mutex = threading.RLock()
        atexit.register(self.flush)

    def record(self, service, operation, payload):
        with self.mutex:
            payload = copy.deepcopy(payload)
            del payload["ResponseMetadata"]["HTTPHeaders"]
            # hack to re-use get_skeleton
            data = {
                "service": service,
                "operation": operation,
                "params": payload,
            }
            skeleton = get_skeleton(data)
            if skeleton in self.skeletons:
                return
            self.skeletons.add(skeleton)
            self.records.append(data)

            if len(self.records) > 50:
                self.flush()

    def flush(self):
        with self.mutex:
            if not self.records:
                return
            try:
                files.mkdir(self.dirpath)
                f = f"responses-{int(time.time())}.pickle"
                with open(os.path.join(self.dirpath, f), "wb") as fd:
                    pickle.dump(self.records, fd)
                    self.records.clear()
            except Exception:
                LOG.exception("error while pickling API response")
