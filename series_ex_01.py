import numpy as np
import pandas as pd

my_numpy_array = np.random.rand(3)

# print(type(my_numpy_array))
# print(my_numpy_array[0])
# print(my_numpy_array[2])

my_series = pd.Series(my_numpy_array, index=["First", "Second", "Third"])
print(my_series)
print(my_series.index)