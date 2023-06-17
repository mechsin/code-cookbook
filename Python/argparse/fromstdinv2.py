#!/usr/bin/env python

# Chris Nyland
# 2022-08-13

# Attempt to create a action to accept the pipe input but
# running it as an environment.

import argparse
import sys

class ExtendFromPipe(argparse._StoreAction):

    def __init__(self, *pargs, delimiter='\n', **kwargs):
        super().__init__(*pargs, **kwargs)
        # Values from STDIN will extend a list so forcing nargs to '*' will
        # ensure this argument always creates a list.
        self.nargs = '*'
        self.delimiter = delimiter

    def __call__(self, parser, namespace, values, option_string=None):
        # Calling super here ensures that there will be a default list
        # After we check to see if the STDIN is coming from a TTY interface
        # if we are being piped information this will be False. We then give
        # a default type conversion if there wasn't one provide and split
        # the input lines from the STDIN and convert them using the type
        # We then get the current value from the name space extend it with
        # the STDIN values and then update the namespace with the new values.
        super().__call__(parser, namespace, values, option_string)
        if not sys.stdin.isatty():
            typecon = self.type if self.type else str
            fromstdin = [typecon(k) for k in sys.stdin.read().splitlines()]
            temp = getattr(namespace, self.dest)
            temp.extend(fromstdin)
            setattr(namespace, self.dest, temp)

if __name__ == "__main__":

    desc = 'Implements Action class that reads from STDIN'
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('--optional', action=ExtendFromPipe)

    cli_args = parser.parse_args()

    print(cli_args.optional)
