import pandas as pd

# Загрузка данных из файла
data = pd.read_csv('no_background.csv')

# Удаление столбца 'space_craft_id'
data.drop('spacecraft_id', axis=1, inplace=True)

# Сохранение изменений в файле
data.to_csv('no_background_no_col.csv', index=False)
