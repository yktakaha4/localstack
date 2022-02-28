import cfnlint.helpers

from localstack.aws.cfn.specs import load_specs


def test_stuff():
    specs = cfnlint.helpers.RESOURCE_SPECS['us-east-1']
    schemas = cfnlint.helpers.REGISTRY_SCHEMAS

    load_specs()

    # for k,v in specs.items():
    #     print(f"{k=}")
    #
    # assert 1 + 1 == 2