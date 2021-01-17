import pandas as pd
import numpy as np

cars_data = pd.read_csv("Toyota.csv", index_col=0, na_values=["??","????"])
cars_data1 = cars_data.copy()
cars_data2 =  cars_data.copy()

# isnull or isna to check NaN na_values

# print(cars_data1.isna().sum())
# print(cars_data2.isnull().sum())

# to get missing values rows
# missing = cars_data2[cars_data2.isnull().any(axis=1)]
# print(missing.shape)
# print(missing.isnull().sum())
# print(missing)
# print(missing.describe())

# mean = cars_data2['Age'].mean()
# cars_data2['Age'].fillna(cars_data2['Age'].mean(), inplace=True)

# print(cars_data2["KM"].mean())
# print(cars_data2["KM"].median())
# cars_data2['KM'].fillna(cars_data2['KM'].median(), inplace=True)

# print(cars_data2['HP'].mean())
# cars_data2['HP'].fillna(cars_data2['HP'].mean(), inplace=True)

# print(cars_data2['FuelType'].value_counts())
# print(cars_data2['FuelType'].value_counts().index[0])
# cars_data2['FuelType'].fillna(cars_data2['FuelType'].value_counts().index[0], inplace=True)
# print(cars_data2.isnull().sum())

# print(cars_data2['MetColor'].value_counts())
# print(cars_data2['MetColor'].mode())
# cars_data2['MetColor'].fillna(cars_data2['MetColor'].mode()[0], inplace=True)
# print(cars_data2.isnull().sum())


cars_data1 = cars_data1.apply(lambda x:x.fillna(x.mean) if x.dtype == 'float' else x.fillna(x.value_counts().index[0]))
print(cars_data1.isnull().sum())
