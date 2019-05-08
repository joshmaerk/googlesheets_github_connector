import os
# from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SPREADSHEET_ID = os.environ.get('SPREADSHEET_ID')
    RANGE_NAME = os.environ.get('RANGE_NAME')
    PATH_TEMPFILE = os.path.join(basedir, 'app/templates/temp_project.html')
    ACCESS_TOKEN = os.environ.get('GIT_ACCESS_TOKEN')
    TARGET_REPO = os.environ.get('GIT_TARGET_REPO')