import argparse
import logging
import os

class LogLevel(argparse.Action):

    def __init__(self, *pargs, default=30, **kwargs):
        kwargs['choices'] = logging._nameToLevel.keys()
        kwargs['default'] = default
        super().__init__(*pargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        lvl = logging._nameToLevel[values]
        setattr(namespace, self.dest, lvl)

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

def FileOrDirectoryType(argstring):
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


