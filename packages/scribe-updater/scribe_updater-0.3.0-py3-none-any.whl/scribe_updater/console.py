import click

from . import __version__
from scribe_updater.updater import Updater

@click.command()
@click.version_option(version=__version__)
@click.option("-t", "--target", help="financial instutions ground truth", required=True)
@click.option("-g", "--ground", help="master ground truth", required=True)
@click.option("-v", "--variables", help="path for the variables csv", required=False)
@click.option("-o", "--output", help="output path for the result", required=True)
@click.option("-m", "--mappings", help="scenario mappings json file for finie versions", required=False)
def main(target, ground, output, mappings={}, variables={}):
    """A tool to update scribe competency configurations."""
    click.echo("updater script my g")
    click.echo(f"target : {target}")
    click.echo(f"ground : {ground}")
    click.echo(f"variables : {variables}")
    click.echo(f"output : {output}")
    click.echo(f"mappings : {mappings}")    
    
    updater = Updater(target, ground, variables, output, mappings)
    