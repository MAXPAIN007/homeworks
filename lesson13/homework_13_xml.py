# Завдання 3:
# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і
# повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо

import xml.etree.ElementTree as ET
import logging
from pathlib import Path


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

folder_path = Path('C:\\Users\\007\\Downloads')
file_path = folder_path /'groups.xml'

def find_timing_exbytes_by_group_number(file_path, group_number):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for group in root.findall('.//group'):
            number = group.find('number')
            if number is not None and number.text == str(group_number):
                # Если номер группы совпадает, ищем значение timingExbytes/incoming
                timing_exbytes = group.find('timingExbytes')
                if timing_exbytes is not None:
                    incoming = timing_exbytes.find('incoming')
                    if incoming is not None:
                        logging.info(f"Значення incoming для group/number {group_number}: {incoming.text}")
                        return incoming.text
                else:
                    logging.info(f"timingExbytes відсутній для group/number {group_number}.")
                    return None

        logging.info(f"Групу з номером {group_number} не знайдено.")
        return None
    except ET.ParseError as e:
        logging.error(f"Помилка парсинга XML файла: {e}")
    except Exception as e:
        logging.error(f"Виникла помилка: {e}")


group_number_to_search = '2'
find_timing_exbytes_by_group_number(file_path, group_number_to_search)