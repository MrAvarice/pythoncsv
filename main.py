# with open("weather_data.csv.csv",) as file:
#     data = file.readlines()
#     print(data)
#
#

# import csv
#
#
# with open("weather_data.csv.csv") as file:
#     data = csv.reader(file)
#     tempertures = []
#     count = 0
#     for row in data:
#         rs = row[1]
#         if rs == "temp":
#             pass
#         else:
#             rt = int(row[1])
#             tempertures.append(rt)
#             print(tempertures)


import pandas

#data = pandas.read_csv("weather_data.csv.csv")

data1 = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


col = data1.groupby('Primary Fur Color').count()
cc = col.to_dict()

data_dict={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [cc['X']['Gray'], cc['X']['Cinnamon'], cc['X']['Black']]
}
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count")
print(df)


# print(data)
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(data["temp"].mean())
#
# m = data["temp"].max()
# # print(data.day)
# #
# d = data[data.temp == m]
# print(d)
#
#
# monday = data[data.day == "Monday"]
# print(monday.condition)

#print(data.temp * 9/5 + 32)

