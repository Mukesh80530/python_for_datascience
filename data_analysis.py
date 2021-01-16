import pandas as pd
import numpy as np


cars_data1= pd.read_csv("Toyota.csv", index_col=0, na_values=["??","????"])
cars_data2 = cars_data1.copy()

# freq_table1 = pd.crosstab(index=cars_data2['FuelType'], columns="count", dropna=True)
# print(freq_table)

# freq_table2 = pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'], dropna=True)
# print(freq_table2)

# freq_table3 = pd.crosstab(
# 	index=cars_data2['Automatic'],
# 	columns=cars_data2['FuelType'], 
# 	margins=True,
# 	dropna=True,
# 	normalize='index'
# 	)
# print(freq_table3)

# freq_table4 = pd.crosstab(
# 	index=cars_data2['Automatic'],
# 	columns=cars_data2['FuelType'], 
# 	margins=True,
# 	dropna=True,
# 	normalize='columns'
# 	)
# print(freq_table4)

numerical_cars_data = cars_data2.select_dtypes(exclude=[object])
# print(numerical_cars_data.shape)
corr_matrix = numerical_cars_data.corr(method='pearson')
print(corr_matrix)