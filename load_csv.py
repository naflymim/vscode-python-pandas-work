import pandas as pd
import os

csv_path = os.path.join(r"I:\Web Developments\Python\VSCode\Panadas\TateGallery", "artwork_data.csv")
# print(csv_path)

df = pd.read_csv(csv_path, nrows=5)
print(df)

df = pd.read_csv(csv_path, nrows=5, index_col='id')
print(df)

cols_to_use = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']
df = pd.read_csv(csv_path, nrows=10, index_col='id', usecols=cols_to_use)
print(df)

df = pd.read_csv(csv_path, index_col='id', usecols=cols_to_use)
df.to_pickle(os.path.join("I:\Web Developments\Python\VSCode\Panadas\TateGallery", "artwork_data_mod.zip"))