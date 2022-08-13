#!/usr/bin/env python

# Christopher Nyland
# 2022-07-13

# Code snippet that shows how to allow an argparse argument input to
# be either a path to a single file or a directory and either way
# return a list of the file paths.

import argparse
import os

def FileOrDirectory(argstring):
    """ Determines if input is a file or directory and returns a list

        This function is meant to be use with the argparse module as a
        argument type. It will determine if the input is a file path
        or directory path and return a list with the file path
        or file paths. The path provided must exist or a parsing
        error will be raised.
    """

    if os.path.isdir(argstring):
        out = [os.path.join(argstring, fn) for fn in os.listdir(argstring)]
    elif os.path.isfile(argstring):
        out = [argstring]
    else:
        raise argparse.ArgumentTypeError('Path is not a file or directory')

    return out


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="File or Directory example")

    kwargs = {
              'help': 'Takes file path or directory',
              'type': FileOrDirectory,
             }
    parser.add_argument('input', **kwargs)

    cli_args = parser.parse_args()

    print(cli_args.input)
