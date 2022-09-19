import json
from pathlib import Path
import os.path

from google.oauth2 import service_account
from dotenv import load_dotenv
cwd = Path().cwd()

load_dotenv()
import os


ADMINS_ID = json.loads(os.getenv('ADMINS_ID'))
BOT_TOKEN = os.getenv('BOT_TOKEN')


REDIS = {
    'db': 2,
    'prefix': cwd.name
}

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/drive.file']


SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), '../', 'credentials.json')

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


category_names = {
    'products': 'Продукти',
    'services': 'Комуналка',
    'relax': 'Відпочинок',
    'cleaning': 'Засоби миття та гігієни',
    'car': 'Витрати на авто',
    'village': 'Витрати на село',
    'credit': 'Погашення кредиту',
    'other': 'Інше'
}

mouth_names = {
    'current': 'поточному місяці',
    'January': 'січні',
    'February': 'лютому',
    'March': 'березні',
    'April': 'квітні',
    'May': 'травні',
    'June': 'червні',
    'July': 'липні',
    'August': 'серпні',
    'September': 'вересні',
    'October': 'жовтні',
    'November': 'листопаді',
    'December': 'грудні',
    '2022': '2022 році',
}
