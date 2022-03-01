import click


def fetch_schema_files(): # TODO
    pass


# TODO: generate diff for schema files
# TODO: create new (overwriting) files in a staging environment first before replacing old ones


@click.command()
@click.argument("service", type=str)
@click.option("--doc/--no-doc", default=False, help="whether or not to generate docstrings")
@click.option(
    "--save/--print",
    default=False,
    help="whether or not to save the result into the api directory",
)
def generate(service: str, doc: bool, save: bool):
    """
    Generate types and API stubs for a given AWS service.

    SERVICE is the service to generate the stubs for (e.g., sqs, or lambda)
    """
    from click import ClickException
    pass


if __name__ == '__main__':
    generate()
