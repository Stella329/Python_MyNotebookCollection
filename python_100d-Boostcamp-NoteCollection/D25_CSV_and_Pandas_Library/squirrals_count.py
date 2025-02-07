# origional CSV: 
# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data

import pandas

## MY VERSION
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

fur_color_data = data['Primary Fur Color']  ## type= data series； get the fur_color column


# TODO group data up by color
## series.groupby(): Group Series
## 单独用groupby，得到的是一个 Groupby 对象。需要加后续函数i.e. describe().unstack()描述组内数据的基本统计量+索引重排; i.e. A.groupby("性别").describe().unstack() -- 描述组内数据的基本统计量+索引重排
## groupby() tricks: https://builtin.com/data-science/pandas-groupby

## series.size(): obtain the number of rows in each group of GroupBy object
## OR series.count(): counts the number of rows in each group

group = data.groupby(fur_color_data)
group_data = group.size()


# TODO build a new dataframe, then save it into a new CSV file
new_dataframe = pandas.DataFrame(group_data)
new_dataframe.to_csv('Fur Color Count')






#ANGELA'S VERSION

#Central Park Squirrel Data Analysis
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")




#OUTPUT
[MY DATAFRAME]
Primary Fur Color,0
Black,103
Cinnamon,392
Gray,2473


[ANGELA'S DATAFRAME]
,Fur Color,Count
0,Gray,2473
1,Cinnamon,392
2,Black,103
