import cfnlint.helpers

def test_stuff():
    specs = cfnlint.helpers.RESOURCE_SPECS

    for k,v in specs.items():
        print(f"{k=}")

    assert 1 + 1 == 2