"""Start the main :mod:`safi` application using the
specified command-line parameters.
"""
import argparse
import logging
import os
import sys

import sq.runtime


DEFAULT_SECRET_KEY = "a4f82ec9800ba3ae40a51717ffb2da128db4f0b25e2f30730c688ccb8e250892"
SECRET_KEY = os.environ.setdefault('SAFI_SECRET_KEY', DEFAULT_SECRET_KEY)
os.environ.setdefault('SAFI_SECRET_KEY', "a4f82ec9800ba3ae40a51717ffb2da128db4f0b25e2f30730c688ccb8e250892")
os.environ.setdefault('SAFI_RDBMS_DSN', "postgresql+psycopg2://safi:safi@rdbms:5432/safi")


class MainProcess(sq.runtime.MainProcess):
    """The main :mod:`safi` process manager."""
    framerate = 10
    components = [
        sq.runtime.HttpServer,
    ]


parser = argparse.ArgumentParser() #pylint: disable=invalid-name
parser.add_argument('-c', dest='config',
    default='./etc/safi.conf',
    help="specifies the runtime configuration file (default: %(default)s)")
parser.add_argument('--loglevel',
    help="specifies the logging verbosity (default: %(default)s)",
    choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'], default='INFO')


if __name__ == '__main__':
    logger = logging.getLogger('safi') #pylint: disable=invalid-name
    args = parser.parse_args() #pylint: disable=invalid-name
    p = MainProcess(args, logger=logger) #pylint: disable=invalid-name

    if DEFAULT_SECRET_KEY == SECRET_KEY:
        logger.critical("The application is started using the default secret key.")


    try:
        sys.exit(p.start() or 0)
    except Exception: #pylint: disable=broad-except
        logger.exception("Fatal exception caused program termination")
        sys.exit(1)


# !!! SG MANAGED FILE -- DO NOT EDIT !!!
