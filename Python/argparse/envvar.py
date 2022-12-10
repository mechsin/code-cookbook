#! /usr/bin/python


# Create an action that allows a command line parameter to default
# to and environmental variable.


import argparse
import os

SENTINEL = object()

class EvnDefault(argparse.Action):

    def __init__(self, *pargs, envvar=None, **kwargs):
        self.envvar = envvar
        super().__init__(*pargs, default=SENTINEL, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if values is None:
            value = os.environ.get(self.envvar)
        breakpoint() 
        setattr(namespace, self.dest, values)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('needed', action=EvnDefault, envvar='SHELL')
    parser.add_argument('--opts', action=EvnDefault, envvar='EDITOR')

    cli_args = parser.parse_args()

    print(cli_args)
