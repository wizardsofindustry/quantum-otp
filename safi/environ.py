"""Environment variables specified by the application Quantumfile."""
import os

import yaml


DEFAULT_SECRET_KEY = "a4f82ec9800ba3ae40a51717ffb2da128db4f0b25e2f30730c688ccb8e250892"

# Set up some variables serving as hints to the Quantum framework.
os.environ['SQ_ENVIRON_PREFIX'] = 'SAFI'


# This is a hook to load secrets or other environment variables
# from YAML-encoded file, for example when using Docker Swarm
# secrets.
if os.getenv('SAFI_SECRETS'):
    with open(os.getenv('SAFI_SECRETS')) as f:
        secrets = yaml.safe_load(f.read()) #pylint: disable=invalid-name
    for key, value in secrets.items():
        if not key.startswith('SAFI'):
            continue
        os.environ[key] = str(value)

    del secrets


# Provide some defaults to the environment prior to assigning the
# module-level constants.
os.environ.setdefault('SAFI_SECRET_KEY',
    "a4f82ec9800ba3ae40a51717ffb2da128db4f0b25e2f30730c688ccb8e250892")
os.environ.setdefault('SAFI_RDBMS_DSN',
    "postgresql+psycopg2://safi:safi@rdbms:5432/safi")
os.environ.setdefault('SAFI_HTTP_ADDR',
    "0.0.0.0")
os.environ.setdefault('SAFI_HTTP_PORT',
    "8443")


SECRET_KEY = os.getenv('SAFI_SECRET_KEY')
RDBMS_DSN = os.getenv('SAFI_RDBMS_DSN')
HTTP_ADDR = os.getenv('SAFI_HTTP_ADDR')
HTTP_PORT = os.getenv('SAFI_HTTP_PORT')
DEPLOYMENT_ENV = os.getenv('QUANTUM_DEPLOYMENT_ENV') or 'production'
CONFIG_DIR = os.getenv('QUANTUM_CONFIG_DIR')
IOC_DIR = os.getenv('QUANTUM_IOC_DIR')
IOC_DEFAULTS = os.getenv('QUANTUM_IOC_DEFAULTS')
TEST_PHASE = os.getenv('SQ_TESTING_PHASE')
