import numpy as np
import pandas as pd

array_2d = np.random.rand(3, 3)
# print(array_2d[0, 1])
# print(array_2d[2, 0])

df = pd.DataFrame(array_2d)
print(df.columns)
print(df)

df.columns = ["First", "Second", "Third"]
print(df.columns)
print(df)
print(df["First"][0])
print(df["Second"][2])
print(df["Third"])

df["Third"].index = ['One', 'Two', 'Three']
print(df["Third"])
print(df)


