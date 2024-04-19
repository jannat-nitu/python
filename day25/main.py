#with open("weather_data.csv") as weather_file:
#    weather = weather_file.#readlines()
#import csv

#with open("weather_data.csv") as data_file:
    #read = csv.reader(data_file)
    #temperatures = []
    #for row in read:
        #if row[1] != "temp":
            #temperatures.append(row[1])
    #print(temperatures)

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur Colors": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel, red_squirrel, black_squirrel]
}
pandas_dataframe = pandas.DataFrame(data_dict)
pandas_dataframe.to_csv("data.csv")


