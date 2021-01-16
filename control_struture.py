import pandas as pd
import numpy as np

# cars_data = pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
cars_data = pd.read_csv('Toyota.csv', index_col=0)
# print(cars_data)
cars_data.insert(10, "Price_Class", " ")

# for i in range(0, len(cars_data['Price']), 1):
# 	if cars_data['Price'][i] <= 8450:
# 		cars_data['Price_Class'][i] = "Low"
# 	elif cars_data['Price'][i] > 11950:
# 		cars_data['Price_Class'][i] = "High"
# 	else:
# 		cars_data['Price_Class'][i] = "Medium"
# print(cars_data)

i = 0
while i < len(cars_data['Price']):
	if cars_data['Price'][i] <= 8450:
		cars_data['Price_Class'][i] = "Low"
	elif cars_data['Price'][i] > 11950:
		cars_data['Price_Class'][i] = "High"
	else:
		cars_data['Price_Class'][i] = "Medium"
	i +=1
# print(cars_data['Price_Class'].value_counts())

cars_data.insert(11, 'Age_converted', 0)

def c_convert(val):
	val_converted = val/12
	return val_converted

cars_data['Age_converted'] = c_convert(cars_data['Age'])
cars_data['Age_converted'] = round(cars_data['Age'], 1)

cars_data.insert(12, "km_per_month", 0)


def c_convert(val1, val2):
	val_converted = val1 / 12
	ratio = val2 /12
	return [val_converted, ratio]


cars_data['Age_converted'], cars_data['km_per_month'] = c_convert(cars_data['Age'], cars_data['KM'])
print(cars_data.head())
