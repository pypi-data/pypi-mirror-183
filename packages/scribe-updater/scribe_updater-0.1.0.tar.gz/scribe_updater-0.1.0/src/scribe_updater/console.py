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
    """The hypermodern Python project."""
    click.echo("updater script my g")
    click.echo(f"target : {target}")
    click.echo(f"ground : {ground}")
    click.echo(f"variables : {variables}")
    click.echo(f"output : {output}")
    click.echo(f"mappings : {mappings}")    
            
    updater = Updater(target, ground, variables, output, mappings)
    updater.update()
    
    
    updater.output
    
    click.echo(f"{output}")
    
    
# def main():
#     parser = argparse.ArgumentParser(description="Parse PBA configuration")

#     parser.add_argument(
#         "--input", help="financial instutions ground truth", required=True
#     )
#     parser.add_argument("--ground", help="master ground truth", required=True)
#     parser.add_argument(
#         "--variables", help="path for the variables csv", required=False
#     )
#     parser.add_argument("--output", help="output path for the result", required=True)
#     parser.add_argument(
#         "--scenario_mappings",
#         help="Scenario Mappings File for Finie Versions JSON",
#         required=False,
#     )

#     # parse command line args and form param to create updated obj
#     args = parser.parse_args()

#     variables = None
#     if args.variables:
#         variables = read_csv(args.variables)

#     target = make_lower(load_json(args.input))
#     ground = make_lower(load_json(args.ground))
#     if args.scenario_mappings:
#         ground_to_target_map = load_json(args.scenario_mappings)
#     else:
#         ground_to_target_map = {}

#     updater = Updater(ground, target, variables, args.output, ground_to_target_map)
#     updater.prep_output_pba()
#     updater.update()
#     updater.output_to_json()
#     updater.get_change_log()


# if __name__ == "__main__":
#     main()
