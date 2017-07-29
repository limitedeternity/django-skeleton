# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import realpath, dirname

PROJECT_DIR = realpath(dirname(dirname(__file__)))
BASE_DIR = realpath(dirname(PROJECT_DIR))
