#!/usr/bin/env python

import argparse
import logging


# It is best to define a logger per module
# We use the name of the module to name the logger this is common 
# convention 
logger = logging.getLogger(__name__)

class LogLevel(argparse.Action):

    def __init__(self, *pargs, default=30, **kwargs):
        kwargs['choices'] = logging._nameToLevel.keys()
        kwargs['default'] = default
        super().__init__(*pargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        lvl = logging._nameToLevel[values]
        setattr(namespace, self.dest, lvl)

def main():
    logger.debug('Prints a debug message')
    logger.info('Prints a info message')
    logger.warning('Prints a warning message')
    logger.error('Prints a error message')
    logger.critical('Prints a critical message')
    
    try:
        raise Exception('Something bad happened')
    except:
        logger.exception('There was a exception here is the traceback')

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--loglevel', action=LogLevel)

    cli_args = parser.parse_args()

    # This gets the root logger. This is the logger that 
    # we will add the handlers to. There are very few
    # reasons to add handlers to any other logger other 
  
    root_logger = logging.getLogger()
    root_logger.setLevel(cli_args.loglevel)
    # Add handlers
    # Handlers are what we use to print the messages to the 
    # screen, write to a file, or send to a network service. 
    # We add handlers to the root logger. There are very few
    # reasons to add handlers to any other logger other. If 
    # you think you need add handlers to another logger 
    # really make sure that its really what you want.

    logging.basicConfig()
    # Now we run the main and you should see the log 
    # messages print but not all of them the log level 
    # of the root logger by default only prints warning messages 
    # and up. 
    loglvlname = logging._levelToName[cli_args.loglevel]
    print('#### Running with log level {} ####'.format(loglvlname))
    main()

