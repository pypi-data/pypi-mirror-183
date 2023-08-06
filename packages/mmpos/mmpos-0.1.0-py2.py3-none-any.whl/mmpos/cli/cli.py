import click
import os
from mmpos.cli.rigs import commands as rigs
from mmpos.cli.farms import commands as farms

@click.group()
def entry_point():
    pass

entry_point.add_command(rigs.entry_point, 'rigs')
entry_point.add_command(farms.entry_point, 'farms')


def main():
    if (not os.environ['MMPOS_API_TOKEN']):
        click.echo("You need to set the env variable MMPOS_API_TOKEN")
        exit(1)

    entry_point()

if __name__ == '__main__':
    main()

