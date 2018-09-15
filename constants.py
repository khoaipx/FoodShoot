import os

SERVICE_IP = '0.0.0.0'
SERVICE_PORT = 12345

PROJECT_DIR = os.path.dirname(os.path.realpath('__file__'))

UPLOAD_FOLDER = os.path.join(PROJECT_DIR, 'upload')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
