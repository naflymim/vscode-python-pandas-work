import pandas as pd
import os

df = pd.read_pickle(r"I:\Web Developments\Python\VSCode\Panadas\TateGallery\artwork_data_mod.zip", "zip")

'''
print(df.columns)
print(df[["artist", "title", "height"]]) '''

artist = df["artist"]
print(len(artist))
print(len(pd.unique(artist)))


'''
for artistName in pd.unique(artist):
    print(artistName)'''