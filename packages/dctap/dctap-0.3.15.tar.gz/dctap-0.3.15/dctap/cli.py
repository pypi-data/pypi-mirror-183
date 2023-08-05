"""DC Tabular Application Profiles (DCTAP) command-line utility."""

import sys
import json as j
from ruamel.yaml import YAML
import click
from .defaults import DEFAULT_CONFIGFILE_NAME, DEFAULT_HIDDEN_CONFIGFILE_NAME
from .config import get_config, write_configfile
from .csvreader import csvreader
from .inspect import pprint_tapshapes, print_warnings
from .loggers import stderr_logger
from .tapclasses import TAPShape, TAPStatementTemplate
from .utils import expand_uri_prefixes

# pylint: disable=unused-argument,no-value-for-parameter
# => unused-argument: Allows placeholders for now.
# => no-value-for-parameter: Okay in cli.py


@click.group()
@click.version_option("0.3.15", help="Show version and exit")
@click.help_option(help="Show help and exit")
@click.pass_context
def cli(context):
    """DC Tabular Application Profiles parser and base module

    Examples (see https://dctap-python.rtfd.io):

    \b
    Write starter config file:
    $ dctap init                           # Write dctap.yaml
    $ dctap init --hidden                  # Write .dctaprc
    \b
    Show normalized view of TAP:
    $ dctap read x.csv                     # Output as plain text
    $ dctap read --json x.csv              # Output as JSON
    $ dctap read --yaml x.csv              # Output as YAML
    $ dctap read --warnings x.csv          # Also show warnings
    """


@cli.command()
@click.option("--hidden", default=False, help="Write as dot file [.dctaprc]")
@click.help_option(help="Show help and exit")
@click.pass_context
def init(context, hidden):
    """Write config file [dctap.yaml]"""
    if hidden:
        configfile = DEFAULT_HIDDEN_CONFIGFILE_NAME
    else:
        configfile = DEFAULT_CONFIGFILE_NAME
    write_configfile(configfile)


@cli.command()
@click.argument("csvfile_obj", type=click.File(mode="r", encoding="utf-8-sig"))
@click.option("--config", type=click.Path(exists=True), help="Alternative config file")
@click.option("--expand-prefixes", is_flag=True, help="Expand compact IRIs")
@click.option("--warnings", is_flag=True, help="Print warnings to stderr")
@click.option("--json", is_flag=True, help="Print JSON to stdout")
@click.option("--yaml", is_flag=True, help="Print YAML to stdout")
@click.help_option(help="Show help and exit")
@click.pass_context
def read(context, csvfile_obj, config, expand_prefixes, warnings, json, yaml):
    """Show TAP as TXT, JSON, or YAML."""
    # pylint: disable=too-many-locals,too-many-arguments

    config_dict = get_config(configfile_name=config)
    tapshapes_dict = csvreader(
        open_csvfile_obj=csvfile_obj,
        config_dict=config_dict,
        shape_class=TAPShape,
        state_class=TAPStatementTemplate,
    )

    if expand_prefixes:
        tapshapes_dict = expand_uri_prefixes(tapshapes_dict, config_dict)

    if json and yaml:
        # Quick fix for mutually exclusive options, a better fix in future.
        echo = stderr_logger()
        echo.warning("Please use either --json or --yaml")
        click.Context.exit(0)

    if json:
        if not warnings:
            del tapshapes_dict["warnings"]
        json_output = j.dumps(tapshapes_dict, indent=2)
        print(json_output)

    if yaml:
        if not warnings:
            del tapshapes_dict["warnings"]
        y = YAML()
        y.indent(mapping=2, sequence=4, offset=2)
        y.dump(tapshapes_dict, sys.stdout)

    if not (json or yaml):
        pprint_output = pprint_tapshapes(
            tapshapes_dict=tapshapes_dict,
            config_dict=config_dict,
            shape_class=TAPShape,
            state_class=TAPStatementTemplate,
        )
        for line in pprint_output:
            print(line, file=sys.stdout)
        if warnings:
            print_warnings(tapshapes_dict["warnings"])
