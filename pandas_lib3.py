import pandas as pd
import numpy as np

cars_data = pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
# print(cars_data.info())
# cars_data['MetColor'] =  cars_data['MetColor'].astype('object')
# cars_data['Automatic'] =  cars_data['Automatic'].astype('object')
# print(cars_data.info())

# print(cars_data['FuelType'].nbytes)
# print(cars_data['FuelType'].astype('category').nbytes)


# print(np.unique(cars_data['Doors']))
# print(np.where(cars_data['Doors']))
# cars_data['Doors'].replace('three', 3, inplace=True)
# cars_data['Doors'].replace('four', 4, inplace=True)
# cars_data['Doors'].replace('five', 5, inplace=True)
# print(np.unique(cars_data['Doors']))

print(cars_data.isnull().sum())