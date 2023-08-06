import os

import click
from config.reader import config_reader
from exceptions.ConfigNotFound import ConfigNotFound


def arg_run(arg2):
    try:
        command = config_reader.get_config_data()["scripts"][arg2]
        print(f"[script] {command} \n")

        os.system(command)
    except ConfigNotFound:
        print("[error] configuration file doesnt exists")
    except KeyError:
        print("[error] script not found")


@click.command()
@click.argument('arg1', required=False)
@click.argument('arg2', required=False)
@click.pass_context
def cli(ctx: any, arg1: str, arg2: str) -> None:
    if arg1 == 'run' and arg2 != None:
        arg_run(arg2)


if __name__ == "__main__":
    cli()
