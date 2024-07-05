import pandas as pd

# Чтение файла no_background.csv
df = pd.read_csv('no_background.csv')  # image_id,spacecraft_id,xmin,ymin,xmax,ymax

# Перевод координат из формата COCO в формат YOLO
df['xmin'] = ((df['xmin'] + df['xmax']) / 2) / 1280
df['ymin'] = ((df['ymin'] + df['ymax']) / 2) / 1024
df['xmax'] = (df['xmax'] - df['xmin']) / 1280
df['ymax'] = (df['ymax'] - df['ymin']) / 1024

# Создание нового файла no_background_yolo.csv
df_yolo = df[['image_id', 'xmin', 'ymin', 'xmax', 'ymax']]
df_yolo.to_csv('no_background_yolo.csv', index=False)
