#!/usr/bin/env python3

"""
This script simply wraps terragrunt (which is a wrapper around terraform...)
and its main function is to allow you to execute a `run-all` command but
broken up in individual steps.

This makes debugging a complex project easier, such as spotting where the
exact problem is.
"""

# idea: parse output
# - https://github.com/bcochofel/terraplanfeed/tree/main/terraplanfeed

import os
import sys
import subprocess
import shlex
import json
import re
import click
import networkx as nx

class Printer():
    """ A simple class for printing nice messages """
    def __init__(
        self,
        verbose: bool,
        ):

        self._print_verbose = verbose

    def header(self, msg):
        msg = msg.strip() if isinstance(msg, str) else msg
        click.secho('\n' + msg, bold=True, file=sys.stderr)

    def verbose(self, msg):
        if self._print_verbose:
            msg = msg.strip() if isinstance(msg, str) else msg
            print(msg, flush=True, file=sys.stderr)

    def normal(self, msg):
        msg = msg.strip() if isinstance(msg, str) else msg
        print(msg, flush=True, file=sys.stderr)

    def bold(self, msg):
        msg = msg.strip() if isinstance(msg, str) else msg
        click.secho('\n' + msg, bold=True, file=sys.stderr)

    def warning(self, msg):
        msg = msg.strip() if isinstance(msg, str) else msg
        click.secho('\n' + msg + '\n', fg="yellow", bold=True, file=sys.stderr)

    def error(self, msg):
        msg = msg.strip() if isinstance(msg, str) else msg
        click.secho(msg, fg="red", bold=True, file=sys.stderr)

    def success(self, msg):
        msg = msg.strip() if isinstance(msg, str) else msg
        click.secho(msg, fg="green", bold=True, file=sys.stderr)

class TgWrap():
    """
    A wrapper around terragrunt with the sole purpose to make it a bit
    (in an opiionated way) easier to use
    """
    SEPARATOR=':|:'

    def __init__(self, verbose):
        self.printer = Printer(verbose)

        # Check if the "TERRAGRUNT_SOURCE" environment variable is set
        env_var = "TERRAGRUNT_SOURCE"
        if env_var in os.environ:
            self.printer.warning(
                f"'{env_var}' environment variable is set with address: '{os.environ[env_var]}'!"
                )
        else:
            self.printer.warning(
                f"No '{env_var}' variable is set, so the sources as defined in terragrunt.hcl files will be used as is!"
                )

    def prepare_groups(self, graph, exclude_external_dependencies):
        """ Prepare the list of groups that will be executed """
        groups = []
        for group in nx.topological_generations(graph):
            try:
                group.remove("\\n") # terragrunt is adding this in some groups for whatever reason
            except ValueError:
                pass
            for idx, directory in enumerate(group):
                if directory.startswith("/") \
                    and exclude_external_dependencies \
                    and directory != os.getcwd():
                    self.printer.verbose(
                        f"- Remove directory from group as it falls out of scope: {directory}"
                        )
                    group[idx] = None
                else:
                    self.printer.verbose(f"+ Include directory: {directory}")

            # remove the null values from the list
            group = list(filter(None, group))
            if len(group) > 0:
                groups.append(group)

        return groups

    def get_di_graph(self, working_dir=None):
        """ Gets the directed graph of terragrunt dependencies, and parse it into a graph object """
        graph = None
        try:
            temp_file = f'{os.environ["TMPDIR"]}tg-dependencies.gv'
            with open(temp_file, 'w', encoding='utf8') as f:
                working_dir_stmt = f'--terragrunt-working-dir {working_dir}' if working_dir else ''
                command = \
                    f'terragrunt graph-dependencies --terragrunt-non-interactive {working_dir_stmt}'
                rc = subprocess.run(
                    shlex.split(command),
                    text=True,
                    stdout=f,
                )
                self.printer.verbose(rc)

            # Read the directed graph and reverse it
            graph = nx.DiGraph(nx.nx_pydot.read_dot(temp_file)).reverse()
        except Exception as e:
            self.printer.error(e)
            raise click.ClickException(e)

        return graph

    def run_di_graph(
        self, command, exclude_external_dependencies, dry_run,
        ask_for_confirmation=False, collect_output_file=None,
        working_dir=None,
        ):
        "Runs the desired command in the directories as defined in the directed graph"
        graph = self.get_di_graph(working_dir=working_dir)

        # first go through the groups and clean up where needed
        groups = self.prepare_groups(
            graph=graph, exclude_external_dependencies=exclude_external_dependencies
            )

        if ask_for_confirmation or self.printer.verbose:
            self.printer.header("The following groups will be processed:")
            for idx, group in enumerate(groups):
                self.printer.normal(f"\nGroup {idx}:")
                for directory in group:
                    self.printer.normal(f"- {directory}")

        if ask_for_confirmation:
            response = input("\nDo you want to continue? (y/n) ")
            if response.lower() != "y":
                sys.exit(1)

        stop_processing = False
        for idx, group in enumerate(groups):
            self.printer.header(f'Group {idx}')
            self.printer.normal(group)

            if command:
                for directory in group:
                    # if we have a specific working dir, and the dir is relative, combine the two
                    if working_dir and not os.path.isabs(directory):
                        directory = os.path.join(working_dir, directory)

                    self.printer.header(
                        f'\n\nStart processing directory: {directory}\n\n'
                        )
                    if dry_run:
                        self.printer.warning(
                            'In dry run mode, no real actions are executed!!'
                            )
                    else:
                        try:
                            if collect_output_file:
                                collect_output_file.write(f'{directory}{self.SEPARATOR}')
                                collect_output_file.flush()
                            temp_file = f'{os.environ["TMPDIR"]}tgwrap-error'
                            messages = ""
                            with open(temp_file, 'w', encoding='utf8') as f:
                                rc = {'returncode': 0}
                                rc = subprocess.run(
                                    shlex.split(command),
                                    text=True,
                                    cwd=directory,
                                    stdout=collect_output_file if collect_output_file else sys.stdout,
                                    stderr=f,
                                )
                                self.printer.verbose(rc)

                            with open(temp_file, 'r', encoding='utf8') as f:
                                messages = f.read()
                            if rc.returncode != 0 or 'error' in messages.lower():
                                raise Exception(
                                    'An error situation detected while processing the terragrunt graph.'
                                    )
                        except FileNotFoundError:
                            self.printer.warning(f'Directory {directory} not found, continue')
                        except Exception as e:
                            self.printer.error(f"Error occurred:\n{str(e)}")
                            self.printer.error("Full stack:")
                            self.printer.normal(messages)

                            stop_processing = True
                            break

            if stop_processing:
                break

    def construct_command(self, command, debug, exclude_external_dependencies,
        non_interactive=True, no_auto_approve=True, no_lock=True, update_source=False,
        working_dir=None, terragrunt_args=()):
        """ Constructs the command """
        commands = {
            'generic': '{base_command} {command} --terragrunt-non-interactive {no_auto_approve} {ignore_deps} {debug_level} {update_source} {working_dir} {terragrunt_args}',
            'info': '{base_command} terragrunt-info --terragrunt-non-interactive {ignore_deps} {debug_level} {update_source} {working_dir} {terragrunt_args}',
            'plan': '{base_command} {command} --terragrunt-non-interactive  -out=planfile {ignore_deps} {debug_level} {lock_level} {update_source} {working_dir} {terragrunt_args}',
            'apply': '{base_command} {command} {non_interactive} {no_auto_approve} --terragrunt-parallelism 1 {ignore_deps} {debug_level} {update_source} {working_dir} {terragrunt_args}',
            'show': '{base_command} {command} --terragrunt-non-interactive {ignore_deps} {update_source} -json planfile', # no working dir!!!
            'destroy': '{base_command} {command} --terragrunt-non-interactive --terragrunt-no-auto-approve {ignore_deps} {debug_level} {working_dir} {terragrunt_args}',
        }

        lock_stmt         = '-lock=false' if no_lock else ''
        update_stmt       = '--terragrunt-source-update' if update_source else ''
        ignore_deps_stmt  = '--terragrunt-ignore-external-dependencies' if exclude_external_dependencies else ''
        debug_stmt        = '--terragrunt-log-level debug --terragrunt-debug' if debug else ''
        auto_approve_stmt = '--terragrunt-no-auto-approve' if no_auto_approve else ''
        interactive_stmt  = '--terragrunt-non-interactive' if non_interactive else ''
        working_dir_stmt  = f'--terragrunt-working-dir {working_dir}' if working_dir else ''

        base_command      = 'terragrunt run-all'

        if command not in ['clean']:
            full_command = commands.get(command, commands.get('generic')).format(
                base_command=base_command,
                command=command,
                lock_level=lock_stmt,
                update_source=update_stmt,
                ignore_deps=ignore_deps_stmt,
                debug_level=debug_stmt,
                no_auto_approve=auto_approve_stmt,
                non_interactive=interactive_stmt,
                working_dir=working_dir_stmt,
                terragrunt_args=' '.join(terragrunt_args),
            )
        else:
            full_command = commands.get(command, commands.get('generic'))

        # remove double spaces
        full_command = re.sub(' +', ' ', full_command)

        self.printer.verbose(f'Full command to execute:\n$ {full_command}')

        return full_command

    def run(self, command, debug, dry_run, no_lock, update_source,
        auto_approve, working_dir, terragrunt_args):
        """ Executes a terragrunt command on a single project """

        self.printer.verbose(f"Attempting to 'run {command}'")
        if terragrunt_args:
            self.printer.verbose(f"- with additional parameters: {' '.join(terragrunt_args)}")

        check_for_file="terragrunt.hcl"
        if working_dir:
            check_for_file = os.path.join(working_dir, check_for_file)
        if not os.path.isfile(check_for_file):
            self.printer.error(
                f"{check_for_file} not found, this seems not to be a terragrunt project directory!"
                )
            sys.exit(1)

        cmd = self.construct_command(
            command=command,
            debug=debug,
            exclude_external_dependencies=True,
            no_lock=no_lock,
            update_source=update_source,
            no_auto_approve=(not auto_approve),
            working_dir=working_dir,
            terragrunt_args=terragrunt_args,
        )

        if dry_run:
            self.printer.warning(f'In dry run mode, no real actions are executed!!')
        else:
            rc = subprocess.run(shlex.split(cmd))
            self.printer.verbose(rc)

    def run_all(self, command, debug, dry_run, no_lock, update_source,
        exclude_external_dependencies, step_by_step, working_dir, terragrunt_args):
        """ Executes a terragrunt command across multiple projects """

        self.printer.verbose(f"Attempting to 'run-all {command}'")
        if terragrunt_args:
            self.printer.verbose(f"- with additional parameters: {' '.join(terragrunt_args)}")

        cmd = self.construct_command(
            command=command,
            debug=debug,
            exclude_external_dependencies=True if step_by_step else exclude_external_dependencies,
            non_interactive=False if command in ['apply', 'destroy'] else True,
            no_lock=no_lock,
            update_source=update_source,
            no_auto_approve=False,
            working_dir=working_dir,
            terragrunt_args=terragrunt_args,
        )

        if step_by_step:
            self.printer.verbose(
                'This command will be executed in each individual project directory!'
                )
            self.run_di_graph(
                command=cmd,
                exclude_external_dependencies=exclude_external_dependencies,
                dry_run=dry_run,
                working_dir=working_dir,
            )
        else:
            if dry_run:
                self.printer.warning('In dry run mode, no real actions are executed!!')
            else:
                rc = subprocess.run(shlex.split(cmd))
                self.printer.verbose(rc)

    def analyze(self, dry_run, exclude_external_dependencies, working_dir, terragrunt_args):
        """ Analyzes the plan files """

        self.printer.verbose("Attempting to 'analyze'")
        if terragrunt_args:
            self.printer.verbose(f"- with additional parameters: {' '.join(terragrunt_args)}")

        # first run a 'show' and write output to file
        cmd = self.construct_command(
            command='show',
            exclude_external_dependencies=exclude_external_dependencies,
            debug=False,
            terragrunt_args=terragrunt_args,
            )

        # then run it and capture the output
        temp_file = f'{os.environ["TMPDIR"]}tgwrap-show'
        json_file = f'{os.environ["TMPDIR"]}planfile.json'
        with open(temp_file, 'w', encoding='utf8') as f:
            self.run_di_graph(
                command=cmd,
                exclude_external_dependencies=exclude_external_dependencies,
                dry_run=dry_run,
                collect_output_file=f,
                working_dir=working_dir,
            )

        ts_validation_successful = True
        with open(temp_file, 'r') as f:
            for line in f:
                split_line = line.split(self.SEPARATOR)
                project = split_line[0]
                plan_file = split_line[1]

                self.printer.header(f"Analyse project: {project}")

                try:
                    d = json.loads(plan_file)

                    if 'resource_changes' in d and len(d['resource_changes']) > 0:
                        self.printer.header('Changes:')

                        changes = False
                        for rc in d['resource_changes']:
                            # check if we do have actual changes
                            actions = rc['change']['actions']
                            if len(actions) == 1 and actions[0] == 'no-op':
                                pass # ignore, just an state change
                            else:
                                self.printer.normal(f'- {rc["address"]}: {",".join(actions)}')
                                changes = True

                        if not changes:
                            print('- no real changes detected.')

                    # if so, write to file
                    with open(json_file, 'w', encoding='utf8') as f:
                        f.write(plan_file)

                    # Check if the "TERRASAFE_CONFIG" environment variable is set
                    env_var = "TERRASAFE_CONFIG"
                    if not env_var in os.environ:
                        self.printer.warning(
                            f"{env_var} environment variable is not set, this is required for running the terrasafe command!"
                            )
                    else:
                        self.printer.header(
                            f"\nRun terrasafe using config {os.environ.get(env_var)}"
                            )

                        cmd = f"cat {json_file} | terrasafe --config {os.environ.get('TERRASAFE_CONFIG')}"
                        output = subprocess.run(
                            cmd,
                            shell=True,
                            text=True,
                            capture_output=True,
                            )
                        if output.returncode != 0:
                            ts_validation_successful = False
                            self.printer.error(output.stdout)
                        elif '0 unauthorized' in output.stdout:
                            self.printer.success(output.stdout)

                except json.decoder.JSONDecodeError as e:
                    raise Exception(
                        f"Planfile for {project} was no proper json, further analysis not possible."
                        ) from e

        if not ts_validation_successful:
            raise Exception("Terrasafe validation failed on one or more projects")
