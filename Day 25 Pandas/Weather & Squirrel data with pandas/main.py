import csv
import pandas 

# # The CSV (Comma Sperated Value ) file has to converted to list then we can work easily.
# # Manullaty convetion with out using pandas library.

# # import csv 
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

# # To make it simple we use pandas
# import pandas 
# data = pandas.read_csv("weather_data.csv")
# # print(type(data)) # Output: <class 'pandas.core.frame.DataFrame'>
# # print(data["temp"]) #Output: Name: temp, dtype: int64
# data_dict = data.to_dict()
# # print(data_dict)
# temp_list = data["temp"].to_list()
# # print(temp_list)
# # print(len(temp_list)) 
# average = sum(temp_list) / len(temp_list)
# # print(average)    # Output: 17.428571428571427
# # print(data["temp"].mean()) # Output: 17.428571428571427
# # print(max(data["temp"])) # Output: 24
# # print(data["temp"].max()) # Output: 24
# # To print COlumns 
# # print(data["condition"]) # By Key 
# # print(data.condition) # By Attribute
# # Get data in row 
# # print(data[data.day == "Monday"])
# # To get max data by row
# # print(data[data.temp == data.temp.max()])

# # monday = data[data.day == "Monday"]
# # print(monday.condition)
# # Convert celuis to farenheit
# monday = data[data.day == "Monday"] 
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# # print(monday_temp_F)

# # Create a data frame from scratch 

# data_dict = {
#     "Students": ["Vinay", "Angela", "Varun"],
#     "Scores": ["76", "56", "65"]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("Pandas_dict.csv")
# # print(data)


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = [data[data["Primary Fur Color"] == "Gray"]]
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"]== "Black"])
print(f" Gray Color Squirrels Count: {gray_squirrels_count}")
print(f" Cinaamon Color Squirrels Count: {cinnamon_squirrels_count}")
print(f" Black Color Squirrels Count: {black_squirrels_count}")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}
print(data_dict)

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("Squirrel_Count.csv")
