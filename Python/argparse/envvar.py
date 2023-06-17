#! /usr/bin/python


# Create an action that allows a command line parameter to default
# to and environmental variable.


import argparse
import os

SENTINEL = object()

class EvnDefault(argparse._StoreAction):

    def __init__(self, *pargs, envvar, **kwargs):
        self.envvar = envvar
        kwargs['required'] = False
        try:
            kwargs['default']  = os.environ[self.envvar]
        except KeyError:
            msg = 'No environmental variable named {}'
            if kwargs['default'] is SENTINEL: 
                raise argparse.ArgumentError(msg.format(envvar))
        super().__init__(*pargs, **kwargs)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    # parser.add_argument('needed', action=EvnDefault, envvar='SHELL')
    parser.add_argument('needed', action=EvnDefault, default=None, envvar='BOB')
    parser.add_argument('--opts', action=EvnDefault, envvar='EDITOR')

    cli_args = parser.parse_args()

    print(cli_args)
