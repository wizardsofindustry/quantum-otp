"""Environment variables specified by the application Quantumfile."""
import os

SECRET_KEY = os.getenv('OTP_SECRET_KEY')
RDBMS_DSN = os.getenv('OTP_RDBMS_DSN')
