import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cars_data1 = pd.read_csv("Toyota.csv", index_col=0, na_values=["??","????"])
cars_data2 = cars_data1.copy()
# print(cars_data2.shape)

# remoing missing values
cars_data2.dropna(axis=0, inplace=True)
print(cars_data2.shape)

plt.scatter(cars_data2['Age'], cars_data2['Price'], c="red")
plt.title('Scatter plot of Price vs Age of the cars')
plt.xlabel("Age(Months)")
plt.ylabel("Price(Euros)")
plt.show()



