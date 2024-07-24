# with open("weather_data.csv", mode="r") as data_file :
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file :
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


#need pandas!

import pandas

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# # temp_list = data["temp"].to_list()
# # total = sum(temp_list)
# # count = len(temp_list)
# # ave = total / count
# # print(ave)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get Data in Columns
# print(data["condition"])
# print(data.condition)

#Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
#
# print(monday.condition)
# monday = int(monday.temp)
# monday_f = monday * 9/5 + 32
#
# print(monday_f)


#Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}
data1 = pandas.DataFrame(data_dict)
data1.to_csv("new_data.csv")