#!/usr/bin/env python3

"""
This script simply wraps terragrunt (which is a wrapper around terraform...)
and its main function is to allow you to execute a `run-all` command but
broken up in individual steps.

This makes debugging a complex project easier, such as spotting where the
exact problem is.
"""

import sys
from importlib.metadata import version, PackageNotFoundError

import click

from outdated import check_outdated # type: ignore

from .main import TgWrap

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = '0.0.0'

def check_latest_version():
    """ check for later versions on pypi """
    try:
        is_outdated, latest_version = check_outdated(__name__, __version__)
        if is_outdated:
            click.echo(
                f'Your local version ({__version__}) is out of date! Latest is {latest_version}!'
            )
    except ValueError:
        # this happens when your local version is ahead of the pypi version,
        # which happens only in development
        pass
    except KeyError:
        click.secho('Could not determine package version, continue nevertheless.', bold=True, file=sys.stderr)
        pass

CLICK_CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

TG_COMMANDS=[
    'init', 'validate', 'validate-inputs', 'plan', 'apply',
    'destroy', 'info', 'output', 'show'
    ]

class DefaultGroup(click.Group):
    '''
    Allow a default command for a group
    '''
    ignore_unknown_options = True

    def __init__(self, *args, **kwargs):
        default_command = kwargs.pop('default_command', None)
        super().__init__(*args, **kwargs)
        self.default_cmd_name = None
        if default_command is not None:
            self.set_default_command(default_command)

    def set_default_command(self, command):
        """ Sets the command that can be omitted (and is considered default) """
        if isinstance(command, str):
            cmd_name = command
        else:
            cmd_name = command.name
            self.add_command(command)
        self.default_cmd_name = cmd_name

    def parse_args(self, ctx, args):
        if not args and self.default_cmd_name is not None:
            args.insert(0, self.default_cmd_name)
        return super().parse_args(ctx, args)

    def get_command(self, ctx, cmd_name):
        if cmd_name not in self.commands and self.default_cmd_name is not None:
            ctx.args0 = cmd_name
            cmd_name = self.default_cmd_name
        return super().get_command(ctx, cmd_name)

    def resolve_command(self, ctx, args):
        cmd_name, cmd, args = super().resolve_command(ctx, args)
        args0 = getattr(ctx, 'args0', None)
        if args0 is not None:
            args.insert(0, args0)
        return cmd_name, cmd, args

@click.group(
    cls=DefaultGroup,
    default_command="run",
    context_settings=CLICK_CONTEXT_SETTINGS,
)
def main():
    pass

@main.command(
    name="run",
    context_settings=dict(
        ignore_unknown_options=True,
    ),
)
@click.argument('command', type=click.Choice(TG_COMMANDS + ['state', 'render-json']))
@click.option('--verbose', '-v', is_flag=True, default=False,
    help='Verbose printing',
    show_default=True
    )
@click.option('--debug', '-d', is_flag=True, default=False,
    help='Run the terragrunt command with debug logging enabled (where applicable)',
    show_default=True
    )
@click.option('--dry-run', '-D', is_flag=True, default=False,
    help='dry-run mode, no real actions are executed (only in combination with step-by-step mode)',
    show_default=True
    )
@click.option('--no-lock', '-n', is_flag=True, default=False,
    help='Do not apply a lock while executing the command (only applicable with plan)',
    show_default=True
    )
@click.option('--update-source', '-u', is_flag=True, default=False,
    help='Run the command including the --terragrunt-source-update option',
    show_default=True
    )
@click.option('--auto-approve', '-a', is_flag=True, default=False,
    help='Do not ask for confirmation before applying planned changes (where applicable)',
    show_default=True
    )
@click.option(
    '--working-dir', '-w', default=None,
    help='Working directory, when omitted the current directory is used',
    )
@click.argument('terragrunt-args', nargs=-1, type=click.UNPROCESSED)
@click.version_option(version=__version__)
def run(command, verbose, debug, dry_run, no_lock, update_source,
    auto_approve, working_dir, terragrunt_args):
    """ [default] Executes a terragrunt command on a single project """

    check_latest_version()

    tgwrap = TgWrap(verbose=verbose)
    tgwrap.run(
        command=command,
        debug=debug,
        dry_run=dry_run,
        no_lock=no_lock,
        update_source=update_source,
        auto_approve=auto_approve,
        working_dir=working_dir,
        terragrunt_args=terragrunt_args,
    )

@main.command(
    name="run-all",
    context_settings=dict(
        ignore_unknown_options=True,
    ),
)
@click.argument('command', type=click.Choice(TG_COMMANDS))
@click.option('--verbose', '-v', is_flag=True, default=False,
    help='Verbose printing',
    show_default=True
    )
@click.option('--debug', '-d', is_flag=True, default=False,
    help='Run the terragrunt command with debug logging enabled (where applicable)',
    show_default=True
    )
@click.option('--dry-run', '-D', is_flag=True, default=False,
    help='dry-run mode, no real actions are executed (only in combination with step-by-step mode)',
    show_default=True
    )
@click.option('--no-lock', '-n', is_flag=True, default=False,
    help='Do not apply a lock while executing the command (only applicable with plan)',
    show_default=True
    )
@click.option('--update-source', '-u', is_flag=True, default=False,
    help='Run the command including the --terragrunt-source-update option',
    show_default=True
    )
@click.option('--exclude-external-dependencies', '-x', is_flag=True, default=False,
    help='Whether or not external dependencies must be ignored',
    show_default=True
    )
@click.option('--step-by-step', '-s', is_flag=True, default=False,
    help='Run the command step by step and stop when an error occurs (where applicable)',
    show_default=True
    )
@click.option(
    '--working-dir', '-w', default=None,
    help='Working directory, when omitted the current directory is used',
    )
@click.argument('terragrunt-args', nargs=-1, type=click.UNPROCESSED)
@click.version_option(version=__version__)
def run_all(command, verbose, debug, dry_run, no_lock, update_source, exclude_external_dependencies,
    step_by_step, working_dir, terragrunt_args):
    """ Executes a terragrunt command across multiple projects """

    check_latest_version()

    tgwrap = TgWrap(verbose=verbose)
    tgwrap.run_all(
        command=command,
        debug=debug,
        dry_run=dry_run,
        no_lock=no_lock,
        update_source=update_source,
        exclude_external_dependencies=exclude_external_dependencies,
        step_by_step=step_by_step,
        working_dir=working_dir,
        terragrunt_args=terragrunt_args,
    )

@main.command(
    name="analyze",
    context_settings=dict(
        ignore_unknown_options=True,
    ),
)
@click.option('--verbose', '-v', is_flag=True, default=False,
    help='Verbose printing',
    show_default=True
    )
@click.option('--dry-run', '-D', is_flag=True, default=False,
    help='dry-run mode, no real actions are executed (only in combination with step-by-step mode)',
    show_default=True
    )
@click.option('--exclude-external-dependencies', '-x', is_flag=True, default=False,
    help='Whether or not external dependencies must be ignored',
    show_default=True
    )
@click.option(
    '--working-dir', '-w', default=None,
    help='Working directory, when omitted the current directory is used',
    )
@click.argument('terragrunt-args', nargs=-1, type=click.UNPROCESSED)
@click.version_option(version=__version__)
def analyze(verbose, dry_run, exclude_external_dependencies, working_dir, terragrunt_args):
    """ Analyzes the plan files """

    check_latest_version()

    tgwrap = TgWrap(verbose=verbose)
    tgwrap.analyze(
        dry_run=dry_run,
        exclude_external_dependencies=exclude_external_dependencies,
        working_dir=working_dir,
        terragrunt_args=terragrunt_args,
    )
