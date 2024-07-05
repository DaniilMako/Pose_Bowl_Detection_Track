import csv
import os


def conver_to_yolo_format(values):
    x_min, y_min, x_max, y_max = values

    # Размеры изображения
    image_width = 1280
    image_height = 1024

    # Вычисляем центр ограничивающего прямоугольника
    x_center = (x_min + x_max) / 2
    y_center = (y_min + y_max) / 2

    # Вычисляем ширину и высоту ограничивающего прямоугольника
    width = x_max - x_min
    height = y_max - y_min

    # Нормализуем координаты и размеры
    x_center /= image_width
    y_center /= image_height
    width /= image_width
    height /= image_height
    return [x_center, y_center, width, height]


# Create labels folder if it doesn't exist
if not os.path.exists('labels/'):
    os.makedirs('labels/')

# Open CSV file
with open('no_background.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip header row

    for _ in range(os.listdir('images')):
        # Iterate through each row in the CSV
        for row in csvreader:
            # Create a filename based on the first column
            filename = row[0] + '.txt'

            # Construct the full path to the labels folder
            filepath = os.path.join('labels', filename)

            # Open the TXT file
            with open(filepath, 'w') as txtfile:
                # Write the formatted row to the TXT file
                values = conver_to_yolo_format(list(map(int, row[1:])))
                txtfile.write('0 ' + ' '.join(map(str, values)))
