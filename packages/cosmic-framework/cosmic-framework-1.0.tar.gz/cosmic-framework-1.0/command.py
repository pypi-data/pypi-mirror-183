import click
from create_files import *

@click.command()
@click.argument("subcommand", required=True)
def celestial(subcommand):
    if subcommand == 'create-files':
        project_name = str(input("What is your project name?"))
        create_app(project_name)
        click.echo("Cool! Your project files have been created")
