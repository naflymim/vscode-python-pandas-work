import pandas as pd
import os

csv_path = r"I:\Web Developments\Python\VSCode\Panadas\TateGallery\artwork_data.csv"

cols_to_use = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']
df = pd.read_csv(csv_path, nrows=10, index_col="id", usecols=cols_to_use)

'''
print(df)
print(type(df.loc[1035].acquisitionYear))
print(type(df.loc[[1044, 1035]]))
print(df.loc[[1044, 1035]])
print(type(df.loc[[1044, 1035]].acquisitionYear))

print(df.loc[1035:1038, ['artist', 'medium', 'acquisitionYear']])
print(type(df.loc[1035:1038, ['artist', 'medium', 'acquisitionYear']]))

print(df['acquisitionYear'] > 1919)
print(df.loc[df['acquisitionYear'] > 1919])'''

print(df.iloc[1:4, 1:2])

df.iloc[0, :]
df.iloc[0:2, 0:2]



