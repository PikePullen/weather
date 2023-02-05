# with open("weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
print("*******************************")
# This is a panda "series" object. A list
print(data["temp"])

print("*******************************")
# This is a panda "dataframe" objects. A sheet in a spreadsheet
print(type(data))

print("*******************************")
# Converts data to dictionary
data_dict = data.to_dict()
print(data_dict)

print("*******************************")
# Converts series to list
temp_list = data["temp"].to_list()
print(temp_list)

print("*******************************")
# Getting the avg of a column/series
# avg_value = sum(temp_list) / len(temp_list)
# print(avg_value)
mean_value = data["temp"].mean()
print(mean_value)

print("*******************************")
# Getting the max of a column/series
max_value = data["temp"].max()
print(max_value)

print("*******************************")
# Getting a column with dot notation. The first one is case-sensitive, the second one is not
print(data["condition"])
print(data.condition)

print("*******************************")
# Get the data in a row
print(data[data.day == "Monday"])
# Get the data in a row, where the temperate was the highest this week
print(data[data.temp == data.temp.max()])

print("*******************************")
# Can assign object to variable, then use dot notation on it
monday = data[data.day == "Monday"]
print(monday.condition)

print("*******************************")
# Create a dataframe, and csv
data_dict2 = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}
mydata = pandas.DataFrame(data_dict2)
print(mydata)
mydata.to_csv("new_data.csv")