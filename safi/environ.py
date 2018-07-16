"""Environment variables specified by the application Quantumfile."""
import os

SECRET_KEY = os.getenv('SAFI_SECRET_KEY')
RDBMS_DSN = os.getenv('SAFI_RDBMS_DSN')
