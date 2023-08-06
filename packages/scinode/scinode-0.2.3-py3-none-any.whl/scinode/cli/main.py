#!/usr/bin/env python
import click
from scinode.cli.commands import daemon, config, node, nodetree, config, web


@click.group(help="CLI tool to manage SciNode")
def cli():
    pass


cli.add_command(daemon.daemon)
cli.add_command(config.config)
cli.add_command(node.node)
cli.add_command(nodetree.nodetree)
cli.add_command(config.config)
cli.add_command(web.web)


if __name__ == "__main__":
    cli()
