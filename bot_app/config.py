import json
from pathlib import Path

from dotenv import load_dotenv
cwd = Path().cwd()

load_dotenv()
import os


ADMINS_ID = json.loads(os.getenv('ADMINS_ID'))
BOT_TOKEN = os.getenv('BOT_TOKEN')
SPREADSHEETS_ID = os.getenv('SAMPLE_SPREADSHEET_ID')

REDIS = {
    'db': 2,
    'prefix': cwd.name
}

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://spreadsheets.google.com/feeds',
          'https://googleapis.com/auth/drive.file', 'https://googleapis.com/auth/drive']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'bot_app/credentials.json')

