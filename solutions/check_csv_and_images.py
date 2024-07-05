import os
import csv


def check_files(csv_file, folder_path):
    # Чтение CSV файла
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        # Пропускаем заголовок
        next(csv_reader)
        # Считаем количество строк
        num_rows = sum(1 for row in csv_reader)

    # Получаем список файлов в папке
    files_in_folder = os.listdir(folder_path)
    print(files_in_folder[:10])
    # Сравниваем количество строк в CSV и количество файлов в папке
    if num_rows != len(files_in_folder):
        print(f"Количество строк в CSV файле не совпадает с количеством файлов в папке: "
              f"{num_rows} в файле и {len(files_in_folder)} в папке")
        return

    # Создаем множество для хранения image_id из CSV файла
    csv_image_ids = set()

    # Читаем CSV файл еще раз, чтобы получить image_id
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        # Пропускаем заголовок
        next(csv_reader)
        # Считываем image_id и добавляем их во множество
        for row in csv_reader:
            csv_image_ids.add(row[0])
        print(csv_image_ids)

    # Проверяем наличие файлов с соответствующими именами в папке
    num_mismatch = 0
    for image_id in csv_image_ids:
        if f"{image_id}.txt" not in files_in_folder:
            num_mismatch += 1
            print(f"Файл с image_id='{image_id}' отсутствует в папке")
    print(f"Число несовпадений: {num_mismatch}")

# Пример использования
csv_file = 'example.csv'
folder_path = 'folder_with_images'
check_files(csv_file, folder_path)
