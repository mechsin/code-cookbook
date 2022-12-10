
import logging

logger = logging.getLogger(__name__)

def a1():
    logger.info('Function a1 runs')

def main():
    logger.info('Run function main')
    a1()
