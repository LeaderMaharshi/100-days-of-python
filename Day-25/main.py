# with open(r"C:\Users\Leader Maharshi\Desktop\python_100_days\Day-25\weather_data.csv") as data:
#     file = data.readlines()
#     print(file)

# import csv

# with open(r"C:\Users\Leader Maharshi\Desktop\python_100_days\Day-25\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas as pd

data = pd.read_csv('Day-25/weather_data.csv')
print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)

# print(data['temp'].mean())

# # Get data in columns
# print(data['condition'])
# print(data.condition)

#get the data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])