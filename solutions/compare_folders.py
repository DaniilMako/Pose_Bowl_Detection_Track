import os


def compare_folders(folder1, folder2):
    # Получаем список базовых имен файлов (без расширений) в первой папке
    files_in_folder1 = {os.path.splitext(file)[0] for file in os.listdir(folder1)}
    # Получаем список базовых имен файлов (без расширений) во второй папке
    files_in_folder2 = {os.path.splitext(file)[0] for file in os.listdir(folder2)}

    # Находим файлы, которые есть в первой папке, но отсутствуют во второй
    files_only_in_folder1 = files_in_folder1 - files_in_folder2
    files_only_in_folder2 = files_in_folder2 - files_in_folder1

    # Выводим результат
    if files_only_in_folder1:
        print(f"Файлы, которые есть в папке {folder1}, но отсутствуют в папке {folder2}:")
        for file in files_only_in_folder1:
            print(file)
    else:
        print(f"Все файлы из папки {folder1} присутствуют в папке {folder2}.")

    if files_only_in_folder2:
        print(f"Файлы, которые есть в папке {folder2}, но отсутствуют в папке {folder1}:")
        for file in files_only_in_folder2:
            print(file)
    else:
        print(f"Все файлы из папки {folder2} присутствуют в папке {folder1}.")


# Пример использования
folder1 = 'images'
folder2 = 'labels'
compare_folders(folder1, folder2)
