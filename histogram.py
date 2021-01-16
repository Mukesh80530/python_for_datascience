import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cars_data1 = pd.read_csv("Toyota.csv", index_col=0, na_values=["??","????"])
cars_data2 = cars_data1.copy()


plt.hist(
	cars_data2['KM'],
	color= "green",
	edgecolor="white",
	bins=5
	)
plt.title("Histogram of kilometer")
plt.xlabel("Kilometer")
plt.ylabel("Frequency")
plt.show()