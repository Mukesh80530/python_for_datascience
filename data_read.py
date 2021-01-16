import os
import pandas as pd

os.chdir('/home/gautam/Desktop')
# data_csv = pd.read_csv('interview_status.csv')
# data_csv = pd.read_csv('interview_status.csv', index_col=0)
# data_csv = pd.read_csv('interview_status.csv', index_col=0, na_values=["??", "###"])
# print(data_csv)

# data_xlsx = pd.read_excel('interview_status_xlsx2.xlsx', index_col=0, na_values=["??","###"])
# print(data_xlsx)

os.chdir("/home/gautam/Desktop/Towards_to_DS")
# data_text =  pd.read_table('Iris_data_sample.txt', sep="\t")
# data_text =  pd.read_table('Iris_data_sample.txt', delimiter="\t")
data_text =  pd.read_table('Iris_data_sample.txt', delimiter=" ")
print(data_text)


