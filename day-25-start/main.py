# with open("./day-25-start/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# from tempfile import TemporaryDirectory

# with open("./day-25-start/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
# data = pandas.read_csv("./day-25-start/weather_data.csv")

# data_to_list = data['temp'].to_list()

# monday = data[data.day == 'Monday']

# f = monday.temp * 9 / 5 + 32

# print(f"{f}f")
