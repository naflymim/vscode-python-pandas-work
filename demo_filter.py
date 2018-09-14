import pandas as pd
import os

df = pd.read_pickle(r"I:\Web Developments\Python\VSCode\Panadas\Demo - Json\TateGallery\artwork_data_mod")

artistFilter = df["artist"] == 'Bacon, Francis'
print(artistFilter.value_counts())

artist_count = df["artist"].value_counts()
print(artist_count)
print(artist_count['Bacon, Francis'])