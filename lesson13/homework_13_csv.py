# Завдання 1 Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність
# дублікатів і приберіть їх. Результат запишіть у файл result_<your_second_name>.csv
from pathlib import Path
import csv

folder_path = Path("C:\\Users\\007\\Downloads")

file1_path = folder_path / 'rmc.csv'
file2_path = folder_path / 'r-m-c.csv'

def creation_unique_file_of_files():
    unique_rows = set()

    def read_csv(file_path):
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            content = csv.reader(file)
            for row in content:
                unique_rows.add(tuple(row))

    read_csv(file1_path)
    read_csv(file2_path)

    result_file_path = folder_path / 'result_ponomarov.csv'
    with open(result_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Запись всех уникальных строк обратно в файл
        for row in unique_rows:
            writer.writerow(row)

    print(f'Результат сохранен в {result_file_path}')

creation_unique_file_of_files()

