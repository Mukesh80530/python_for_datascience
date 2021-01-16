import os
import pandas as pd
import numpy as np


# cars_data = pd.read_csv('Toyota.csv')
cars_data = pd.read_csv('Toyota.csv', index_col=0)
sample_data = cars_data.copy(deep=False)


# print(sample_data.index)
# print(sample_data.columns)
# print(sample_data.size)
# print(sample_data.shape)
# print(sample_data.memory_usage())
# print(cars_data.ndim)
# print(cars_data.head(7))
# print(cars_data.tail(5))
# print(cars_data.at[4, 'FuelType'])
# print(cars_data.iat[4,3])
# print(cars_data.loc[:,"FuelType"])
# print(cars_data.loc[:,"FuelType"])