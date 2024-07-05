import os
import csv


def create_csv_with_labels(folder_path, csv_file):
    # Открываем CSV файл для записи
    with open(csv_file, 'w', newline='') as csvfile:
        fieldnames = ['image_id', 'xmin', 'ymin', 'xmax', 'ymax']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Получаем список файлов в папке
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        # Обходим каждый файл
        for file_name in files:
            # Проверяем, что файл имеет расширение txt
            if file_name.endswith('.txt'):
                image_id = os.path.splitext(file_name)[0]  # Получаем название файла без расширения

                # Открываем файл и считываем последнюю строку
                with open(os.path.join(folder_path, file_name), 'r') as file:
                    lines = file.readlines()
                    last_line = lines[-1].strip().split()

                    # Проверяем, что в последней строке есть 5 значений
                    if len(last_line) == 5:
                        xmin, ymin, xmax, ymax = last_line[1:]
                        # Записываем данные в CSV файл
                        writer.writerow({'image_id': image_id, 'xmin': xmin, 'ymin': ymin, 'xmax': xmax, 'ymax': ymax})


# Пример использования
folder_path = 'labels'
csv_file = 'labels.csv'
create_csv_with_labels(folder_path, csv_file)
