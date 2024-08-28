# Завдання 2:
# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
# результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log

import logging
import json
from pathlib import Path

logging.basicConfig(
    filename='json__ponomarov.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

folder_path = Path('https://github.com/dntpanix/automation_qa/tree/0c61017dfea127e5e4a048bfc411f07e1c324b27/ideas_for_test/work_with_json')

def validate_json_files(folder_path):
    for file_path in folder_path.glob('*.json'):
        try:
            if file_path.suffix == '.json':
                with open(file_path, 'r', encoding='utf-8') as file:
                    json.load(file)
            else:
                raise ValueError (f'Файл {file_path} не является файлом JSON')
        except (json.JSONDecodeError, IOError, ValueError) as e:
            logging.error(f'Невалидный JSON файл: {file_path}, Ошибка: {e}')

validate_json_files(folder_path)


