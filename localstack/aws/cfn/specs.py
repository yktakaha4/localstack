import json
import logging
import os
import cfnlint
import cfnlint.core as core

SPECS = {}
SCHEMAS = {}
MERGED = {}  # resource type => spec + schema

def load_specs():
    global SPECS
    SPECS = cfnlint.helpers.RESOURCE_SPECS['us-east-1']

    rootdir = os.path.join(os.path.dirname(__file__), "schemas")
    files = os.listdir(rootdir)
    for file in files:
        if "__init__" not in file and file.endswith(".json"):
            with open(os.path.join(rootdir, file), "r") as f:
                try:
                    current_type = json.load(f)
                    SCHEMAS[current_type["typeName"]] = current_type
                except Exception as e:
                    print(f"FAILED FOR file: {file}")
                    logging.error(e)

    for k, v in SPECS.items():
        MERGED[k] = {
            "schema": SCHEMAS.get(k),
            "specs": v
        }

    SUPPORTED_SCHEMAS = {k: v for k, v in SCHEMAS.items() if v.get('handlers')}
    UNSUPPORTED_SCHEMAS = {}
    for k, v in SCHEMAS.items():
        if not v.get('handlers'):
            subdir = UNSUPPORTED_SCHEMAS.setdefault(k.split("::")[1], {})
            subdir[k] = v

    print(f"Supported schemas: {len(SUPPORTED_SCHEMAS)=}")
    print(f"merged size: {len(MERGED)=}")


    filename = "/home/dominik/work/localstack/localstack/localstack/aws/cfn/cdk_bootstrap_v10.yaml"
    (args, filenames, formatter) = core.get_args_filenames([filename])
    (template, rules, errors) = core.get_template_rules(filename, args)
    template_obj = cfnlint.template.Template(filename, template)
    graph = cfnlint.graph.Graph(template_obj)

    # simulated deployment loop

    assert graph.graph.is_directed()

    # first get all nodes without incoming edges
    roots = [k for k,v in graph.graph.in_degree() if v == 0]
    for root in roots:
        # deploy this resource
        print(f"deploying L1 {root}")

    # TODO: take different approach here by waiting for a finish event (CREATE_COMPLETE or error)



