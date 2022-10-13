from __future__ import print_function

import os.path

from googleapiclient import discovery
from bot_app import config

SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
service = discovery.build('sheets', 'v4', credentials=config.credentials).spreadsheets().values()


async def set_current_range_expenses(date_mes):
    """
    Установка области внесения данных по расходам в таблицу в формате: название_листа!диапазон

    :param date_mes: дата (str)
    :return: srt
    """
    current_month = date_mes.strftime('%B')
    result = f'{current_month}!A7:L1000'
    return result


async def set_current_range_profit(date_mes):
    """
    Установка области внесения данных по доходам в таблицу в формате: название_листа!диапазон

    :param date_mes: дата (str)
    :return: srt
    """
    current_month = date_mes.strftime('%B')
    result = f'{current_month}!A7:D1000'
    return result


async def add_new_row(range, array):
    """
    Добавление новой строки в таблицу

    :param range: область внесения данных (str)
    :param array: значения (dict)
    :return: None
    """
    result = service.append(spreadsheetId=SPREADSHEET_ID,
                            range=range,
                            valueInputOption='USER_ENTERED',
                            insertDataOption='INSERT_ROWS',
                            body=array).execute()


async def get_data_for_month(month):
    """
    Получение данных их таблицы по году

    :param month: название листа (str)
    :return: str
    """
    result = service.get(spreadsheetId=SPREADSHEET_ID,
                         range=month).execute()
    if int(result['values'][0][2]) or int(result['values'][2][2]) != 0:
        result_text = f"\n{'Загальний баланс:':45}<b>{result['values'][0][2]}</b>\n" \
                      f"----------\n" \
                      f"{'Дохід:':57}{result['values'][1][2]}\n" \
                      f"----------\n" \
                      f"{'Витрати всього:':48}{result['values'][2][2]}\n\n" \
                      f"Розподіл витрат:\n\n" \
                      f"{'Продукти харчування:':41}{result['values'][3][4]}\n" \
                      f"{'Комунальні витрати:':43}{result['values'][3][5]}\n" \
                      f"{'Відпочинок:':51}{result['values'][3][6]}\n" \
                      f"{'Витрати на миючі засоби:':39}{result['values'][3][7]}\n" \
                      f"{'Витрати на автомобіль:':41}{result['values'][3][8]}\n" \
                      f"{'Витрати на село:':48}{result['values'][3][9]}\n" \
                      f"{'Погашення кредиту:':43}{result['values'][3][10]}\n" \
                      f"{'Інші витрати:':51}{result['values'][3][11]}\n"
        return result_text
    return 'Інформація відсутня'


async def get_data_for_year(year):
    """
    Получение данных их таблицы по месяцу

    :param year: str
    :return: str
    """
    result = service.get(spreadsheetId=SPREADSHEET_ID,
                         range=year).execute()
    result_text = f"\n{'Загальний баланс:':45}<b>{result['values'][0][1]}</b>\n" \
                  f"{'Дохід:':57}{result['values'][1][1]}\n" \
                  f"{'Витрати всього:':48}{result['values'][2][1]}\n\n" \
                  f"Розподіл витрат по категоріям:\n" \
                  f"{'Продукти харчування:':41}{result['values'][19][1]}\n" \
                  f"{'Комунальні витрати:':43}{result['values'][19][2]}\n" \
                  f"{'Відпочинок:':51}{result['values'][19][3]}\n" \
                  f"{'Витрати на миючі засоби:':39}{result['values'][19][4]}\n" \
                  f"{'Витрати на автомобіль:':41}{result['values'][19][5]}\n" \
                  f"{'Витрати на село:':48}{result['values'][19][6]}\n" \
                  f"{'Погашення кредиту:':43}{result['values'][19][7]}\n" \
                  f"{'Інші витрати:':51}{result['values'][19][8]}\n"
    return result_text




# response = service.update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                          range=range_,
#                          valueInputOption='USER_ENTERED',
#                          body=array).execute()

# Call the Sheets API
# result = service.get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
# # data_from_sheet = result.get('values', [])
#  new = service.get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='09!C1').execute()
# print(new.values())
