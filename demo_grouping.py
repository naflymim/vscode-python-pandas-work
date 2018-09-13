import pandas as pd
import os
import numpy as np

csv_path = os.path.join(r"I:\Web Developments\Python\VSCode\Panadas\Demo - Json\TateGallery", "artwork_data.csv")

cols_to_use = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']
df = pd.read_csv(csv_path, index_col='id', usecols=cols_to_use)

'''
print(df.groupby('artist'))
print(df.describe(include='all'))
print(df.describe(include=[np.number]))'''

#Get the copy of the data
small_df = df.iloc[49980:50019, :].copy()
#print(small_df)

#Grouping the data
'''
grouped = small_df.groupby('artist')
for name, group_df in grouped:
    print(name)
    print(group_df)'''

grouped = small_df.groupby('artist')
'''
for name, groupby_df in grouped:
    min_year = groupby_df['acquisitionYear'].min()
    print("{}: {}".format(name, min_year))'''


def fiil_values(series):      
    # Get the value count for the Medium series
    values_counted = series.value_counts(ascending=False)      
    if values_counted.empty:
        return series
   
    #If the value count is desending order get the most  used one by refering firts index 
    most_frequent = values_counted.index[0]   

    #Fill NA/NaN values using the specified method
    new_medium = series.fillna(most_frequent)    
    return new_medium

grouped_medium = small_df.groupby('artist')['medium']
small_df.loc[:, 'medium'] = grouped_medium.transform(fiil_values)

#Min
df.groupby('artist').agg(np.min)
df.groupby('artist').min()

#Filter
grouped_title = df.groupby('title')
title_count = grouped_title.size().sort_values(ascending=False) 
print(title_count)
