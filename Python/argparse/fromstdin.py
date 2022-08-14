#!/usr/bin/env python

# Chris Nyland
# 2022-08-13

# Argparse example of how to read in values from a piped STDIN

import argparse
import sys

if __name__ == '__main__':
    # Below we setup a parser with just one argument. This argument will
    # collect all input in to a list. Additionally after input is parsed
    # we extend the list by parsing the STDIN stream. Any piped data will
    # come from this stream.

    desc = 'Accept input interactively or via pipe'
    parser = argparse.ArgumentParser(description=desc)

    kwargs = {
              'nargs': '*',
              'default': list(),
             }

    parser.add_argument('files', **kwargs)

    cli_args = parser.parse_args()

    # We check to make sure STDIN is no a TTY interface because if it
    # is it isn't a piped stream. As long as it is not we read the
    # stream and split on the new lines PIPED streams sometimes have
    # blanks in the so we remove them.
    if not sys.stdin.isatty():
        temp = [k for k in sys.stdin.read().splitlines() if k]
        cli_args.files.extend(temp)

    print(cli_args.files)
