import click

from yagc.git.branch_validator import BranchValidator


@click.command()
@click.option("--branch-name", help="The name of your branch")
def main(branch_name):
    """Validate that the branch is correct."""
    if branch_name is None:
        raise click.UsageError("Please provide a branch name")
    if BranchValidator(branch_name).valid_branch():
        click.echo("Branch is valid")
    else:
        raise click.UsageError("Branch is invalid")
