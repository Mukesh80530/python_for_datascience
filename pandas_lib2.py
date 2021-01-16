import os
import pandas as pd
import numpy as np

# cars_data = pd.read_csv('Toyota.csv')
cars_data = pd.read_csv('Toyota.csv', index_col=0)
# sample_data = cars_data.copy(deep=False)

# print(sample_data.dtypes)
# print(sample_data.get_dtype_counts())
# print(sample_data.select_dtypes(exclude=['int64']))
# print(sample_data.select_dtypes(include=['int64']))
# print(cars_data.info())
# print(np.unique(cars_data['KM']))
# print(np.unique(cars_data['HP']))
# print(np.unique(cars_data['MetColor']))
# print(np.unique(cars_data['Automatic']))
# print(np.unique(cars_data['Doors']))