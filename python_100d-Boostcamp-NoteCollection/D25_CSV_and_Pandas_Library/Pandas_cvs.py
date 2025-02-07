#-------------------------PANDA DATA STRUCTURE------------------------#

# 简单类型见excel笔记
# panda doc: https://pandas.pydata.org/docs/reference/index.html

# data structure (data type):
# 1. dataframe: spreadsheet, csv, tables etc.
# 2. series: i.e. a single column


# 查看dataframe数据明细+类型
df.info()
df.dtypes() #--查看数据类型

type(df['column_name']) #--查看一列
type(df['column_name1', 'column_name2'... ])#--查看多列

df.head(10) #--前10 rows
df.tail(10) #--尾10 rows


# -----------------------------INDEX-------------------------------#
# The index information contains the labels of the rows.

import pandas as pd
df = pd.read_csv('data.csv')
print(df.index)
# -- RangeIndex(start=0, stop=169, step=1)

df_length = len(DataFrame.index)
# get the number of rows using len(DataFrame.index) 
# for determining the position at which we need to add the new row.


# i.e.2
df.index = [100, 200, 300]
# df
#     Name  Age Location
# 100  Alice   25  Seattle
# 200    Bob   30 New York
# 300  Aritra  35    Kona


# RESET_INDEX: 
set_index() vs. reset_index(): 
# https://blog.csdn.net/jingyi130705008/article/details/78162758
reset_index()
#可分为两种类型: 第一种是对原来的数据表进行reset还原索引，重新变为默认的整型索引；第二种是对使用过set_index()函数的数据表进行reset。




#-------------------------FILES: OPEN/READ-------------------------#

# GENERAL CREATE/OPEN

f = open("demofile3.txt", "r")
f.write("Now the file has more content!")
f.close()

# OR
with open('file_name.txt', 'a') as file:
    file.write ('write something in the file') 
    ## will close the file automatically when ending
    ## append: 第一次创建，第2+次append at the end of the file


# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content


# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist



#--------------------------READ/SAVE CSV------------------------#

# READ CSV----------------------------------

# METHOD 1: using CSV

import csv
with open ('weather_data.csv') as data_file:
    weather_data = csv.reader(data_file)   ## create a csv_reader object
## 如果只是file而非csv，则不import csv 



# METHOD 2: Using pandas.csv_reader()

import pandas
dataframe = pandas.read_csv ('data/french_words.csv') ##return type=df

## --> returns a dataframe object, which is a two-dimensional table with rows and columns
# i.e. 
data = pandas.read_csv('weather_data.csv',index_col=[0])  ## TABLE
temperature = data ['temp'] ## COLUMN


# SAVE AS CSV------------------------------------------

## from dataframe
df = pandas.DataFrame(states_list)
df.to_csv('states_to_learn.csv', index=False)
## if not index=False, 每当pandas创建一个df,就会自动加上一次index;在后续save时不会自动删除


# from a dictionary
data.to_csv("filename.csv", index=False)



# OPEN EXCEL------------------------------------------
excel = pandas.read_excel ('name.xlsx', sheet_name = 'set your sheet name')
## sheet_name 默认为sheet1, 有value为改名

# SAVE AS EXCEL
file.to_excel ('name.xlsx', sheet_name='name',index=False)




# ERROR 1: IF AN EMPTY FILE in the beginning ---------------------------------------
## 重要！!!! read_csv and read_table do not work on empty files.

try: # 判断是否为空，需要首次创建：
    pw_table = pandas.read_csv('my_password_notebook.csv')
except pandas.errors.EmptyDataError or FileNotFoundError:
    default = {'website': [None],
        'Email/Username': [None],
        'password': [None]
        }
    pw_df = pandas.DataFrame(default)
else:
    pw_df = pandas.DataFrame(pw_table)


# EEROR 2: --ValueError: If using all scalar values, you must pass an index
# 通过字典来创建DataFrame对象: 直接传入标称属性为value的字典需要写入index，也就是说，需要在创建DataFrame对象时设定index
import pandas as pd

#方法一：直接在创建DataFrame时设置index即可
dict = {'a':1,'b':2,'c':3}
data = pd.DataFrame(dict,index=[0])
#OR
data = pd.DataFrame(dict,index=False)
print(data)

#方法二：通过from_dict函数将value为标称变量的字典转换为DataFrame对象
dict = {'a':1,'b':2,'c':3}
pd.DataFrame.from_dict(dict,orient='index').T
print(data)

#方法三！！！：输入字典时不要让Value为标称属性，把Value转换为list对象再传入即可
dict = {'a':[1],'b':[2],'c':[3]}
data = pd.DataFrame(dict)
print(data)

#方法四：直接将key和value取出来，都转换成list对象
dict = {'a':1,'b':2,'c':3}
pd.DataFrame(list(dict.items()))
print(data)








#------------------------------------DATAFRAME--------------------------------------#

#CREATE AND CONVERT
## TODO create a dataframe from scratch; TODO convert df into other forms

data_dict = {  ## i.e.
    'student':['Ted','Stella']
    'score':[60,90]
}
data = pandas.DataFrame(data_dict)
data.to_csv("data/filename.csv", index=False)  ## type: data=dataframe

# call pandas library, get hold of DataFrame class, and initialize it with data (data_dict)
# convert the dataframe(dictionary) into csv file, which will create a new csv file with all data created automatically.
# input: take input of the path you wanna save this file to
# INDEX: If you don't want to create an index for the new csv, you can set the index parameter to False




# TODO CONVERT list/dict into df

## CONVERT a list of str into panda Dataframe
list = df.to_list()

## CONVERT Dataframe into dictionary 
dict = DataFrame.to_dict(orient="records")
    ## To get all rows out as a list of dictionaries e.g. [{french_word: english_word}, {french_word2: english_word2}, {french_word3: english_word3}]
    ## --若转化成其他格式，见url: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html



# ---------------完整例子
import pandas as pd

#create dictionary of students
my_dict = {
      "Student": ['John', 'Lexi', 'Augustin', 'Jane', 'Kate'],
      "Age": [18, 17, 19, 17, 18]
   }

#create data frame from dictionary
classA = pd.DataFrame(my_dict)

#save dataframe to csv file
classA.to_csv("student.csv", index=False)

#validate the csv file by importing it
print(pd.read_csv("student.csv"))

# append a df to an existing CSV: 具体例子见D29 password generator
df.to_csv('log.csv', mode='a', index=False, header=False)






#-------------------------DATATYPE-------------------------#

# The default data type in NumPy is float_. 但由于不是内置，所以df.dtypes()会告诉你为object其实不是
## !! some operations in pandas can change dtypes
## https://numpy.org/doc/stable/reference/arrays.scalars.html#  OR  https://pbpython.com/pandas_dtypes.html


# CONVERT

df['column_name'].astype('string')
# Convert the 'column_name' column to string
## dtype: object  -- meaning string

df['your_column'].astype('Int64').astype('str')
#OR
df.astype(float).sum().astype(int).astype(str)
# it will properly convert 1.0 to 1.







#-------------------------CALL THE DATA SERIES-------------------------#
##METHOD 1: readlines()

with (open('weather_data.csv') as weather_data):
    data = weather_data.readlines()
    weather_data_list = []
    for item in data:
        stripped_item = item.strip() ## get rid of '\n'
        weather_data_list = []
        weather_data_list.append(stripped_item)

# print(weather_data_list) 所有数据都在一个list中,并in string format，需要额外clean：
# ['day,temp,condition', 'Monday,12,Sunny', 'Tuesday,14,Rain', 'Wednesday,15,Rain',...]



##METHOD 2: using built-in CSV reading and writing library -- much faff!!
# put all lines in CSV into seperated lists

import csv

with open('weather_data.csv') as data_file:
    weather_data = csv.reader(data_file)  ## create a csv.reader object, can be using more methods on

    temperature_list = []
    for item in weather_data:  ## item = ['day', 'temp', 'condition'] and more -- lists; each line is a seperated list
        if item[1] == 'temp': ##title colomn label；item[1]=temp
            pass
        else:
            temperature = int(item[1])
            temperature_list.append(temperature)
    print(temperature_list)  ## [12, 14, 15, 14, 21, 22, 24]

#METHOD 3: using Panda
import pandas
data = pandas.read_csv('weather_data.csv') ## table








#------------------------Pandas READ/ADD----------------------------#
#-------------------------READ A COLUMN-------------------------#

# 选择一列
## METHOD 1: treating the data as a dictionary
temp = df['temp']

## METHOD 2: treating the data as an object
## --pandas has turn each colum into a data attribute. So can call the attribute directly
temp= df.temp


# 选择多列
multi_colums = df['column_name1', 'column_name2'... ]


#-------------------------ADD NEW COLUMNS-------------------------#

# methods: https://www.geeksforgeeks.org/adding-new-column-to-existing-dataframe-in-pandas/

## METHOD 1: Add a New Column to an Existing Dataframe using DataFrame.insert()
    DataFrame.insert()

    df.insert (
    location = int(the location of column where we want to insert new column), 
    column=a string which is name of column to be inserted, 
    vaule=the value to be inserted, allow_duplicates=boolean value which checks if column with same name already exists or not)
    # https://www.geeksforgeeks.org/python-pandas-dataframe-insert/

    # i.e. 1 --Add Extra Column with Static Value
    static_value = 'Male'
    df['occupation'] = static_value

    #  age     name address occupation
    # 0   21  Pratham      MP       Male
    # 1   22  Shivang   Delhi       Male
    # 2   27    Suraj      UP       Male


    # i.e.2 
    # Define a dictionary containing Students data
    data = {
        'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']
    }
    # Convert the dictionary into DataFrame
    df = pd.DataFrame(data)
    
    # Using DataFrame.insert() to add a column
    df.insert(2, "Age", [21, 23, 24, 21], True)




## METHOD 2: Add Column to DataFrame using a Dictionary
    # Import pandas package
    import pandas as pd
    
    # Define a dictionary containing Students data
    data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
            'Height': [5.1, 6.2, 5.1, 5.2],
            'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
    
    # Define a dictionary with key values of an existing column and their respective value pairs as the values for our new column.
    address = {'Delhi': 'Jai', 'Bangalore': 'Princi',
            'Patna': 'Gaurav', 'Chennai': 'Anuj'}
    
    # Convert the dictionary into DataFrame
    df = pd.DataFrame(data)
    
    # Provide 'Address' as the column name
    df['Address'] = address



## METHOD 3:Adding a New Column to a Pandas DataFrame using List

    # Declare a list that is to be converted into a column
    address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
    
    # Using 'Address' as the column name
    # and equating it to the list
    df['Address'] = address

    # Name  Height Qualification    Address
    # 0     Jai     5.1           Msc      Delhi
    # 1  Princi     6.2            MA  Bangalore
    # 2  Gaurav     5.1           Msc    Chennai
    # 3    Anuj     5.2           Msc      Patna




#-------------------------READ A ROW-------------------------#


# READ A ROW:  
# METHOD 1： get data from a row -- by filtering the column !!!
    data[data.day == 'Monday']
    ## OR
    data[data['day']=='Monday']

    #print out:
    #       day  temp condition
    # 0  Monday    12     Sunny

# i.e.2 an ROW example from the Guess States Names 
    column2 = data.state  ## all column
    row31 = data[data.state == user_answer] 
    ## specific rows -- pull out the row where state == user_answer state
    
    #     state    x    y
    # 31  New York 236 104

    pen.goto(int(row31.x), int(row31.y)) 
    ## tap into the attributions using the names of the columns !!!
    pen.write(row31.state)  ## the cell
    pen.write(row31.state.item()) ## no spelling format request
    # Series.item(): 标量无方向= raw value!!! --return the first element of the given series object as a scalar!!!


# METHOD 2: 
    DataFrame.loc[]
    ## https://www.geeksforgeeks.org/python-pandas-dataframe-loc/

    # i.e. 
    ## Declare a list that is to be converted into a column
    address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
    
    # Using 'Address' as the column name
    # and equating it to the list
    df['Address'] = address



#-------------------------ADD NEW ROWS-------------------------#

# SELECTION METHODS   -------------------------------------------
df.loc[index] # row with index i will be what you specify it to be in the dataframe
df.iloc[] # are for position numbers
# Note: df.append() has been removed!!!!!!




# METHOD 1: add the row to the end of df
df.loc[len(df)] = new_row

    #i.e.
    import pandas as pd 
    dict = {'Name':['Martha', 'Tim', 'Rob', 'Georgia'], 
            'Maths':[87, 91, 97, 95], 
            'Science':[83, 99, 84, 76] 
        } 
    df = pd.DataFrame(dict) 

    df.loc[len(df.index)] = ['Amy', 89, 93]  
    #--add the row at the last in dataframe
    #==df.loc[df.index.max() + 1] = ['Amy', 89, 93]  

# METHOD 2: Append using list  
list = []

for new_row in items_generation_logic:
    list.append(new_row)

# create extension
df_extended = pd.DataFrame(list, columns=['A', 'B', 'C'])
# or columns=df.columns if identical columns

# concatenate to original
out = pd.concat([df, df_extended])


#-------------------------pandas.concat()------------------------#
pandas.concat()
# concatenate everything； -- vs. pandas.merge(); pandas.join()
# https://www.geeksforgeeks.org/pandas-concat-function-in-python/





#-------------------------DELETE COLUMNS/ROWS-------------------------#

panda.df.drop()
# panda doc: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html


# COLUMN ------------------------------------------
# DROP THE WHOLE COLUMNS
df = df.drop('column_name', axis=1)
# where 1 is the axis number (0 for rows and 1 for columns.)

# DROP SEVERAL COLUMNS
df = df.drop(columns=['column_nameA', 'column_nameB'])



# DROP by column number instead of by column label
# e.g. the 1st, 2nd and 4th columns

df = df.drop(df.columns[[0, 1, 3]], axis=1)  
# --df.columns is zero-based pd.Index

df.drop(['column_nameA', 'column_nameB'], axis=1, inplace=True)




# DROP ROWS ------------------------------------------

# Drop a row by index
df.drop([0, 1])
#    A  B   C   D
# 2  8  9  10  11


# Delete rows: Specify by row name (label)
print(df.drop('Charlie', axis=0))
# =
print(df.drop(['Bob', 'Dave', 'Frank']))






#-------------------------OTHER METHODS-------------------------#


## TODO : turn the column into a Python list
temp_list = data['temp'].to_list() ## turn 'temp' series into python list; print out [12, 14, 15, 14, 21, 22, 24]



## TODO : get the average temperature
## Python Average: Len() and Sum()
avg_temp = sum(temp_list)/len(temp_list)

## ALTERNATIVE: pandas
##Series.mean([axis, skipna, numeric_only]) -- Return the mean of the values over the requested axis.
data['temp'].mean()



## TODO : get the maximum temp in the column
data['temp'].max()



# TODO : which row of data has the highest temp
highest_temp = data.temp.max()
print(data[data.temp==highest_temp])



## TODO : tap into the values under a certain column in a row (row + column)
monday = data[data.day == 'Monday'] ## row
monday.temp  ## row+ column ## 0   12
monday.temp[0] ## 12  -- WHY [0]??? I've rasied a question in Coursa

monday.condition ## 0   sunny



# TODO OVERWRITE COLUMN VALUES
df.assign(**kwargs) 
#assigns new columns to a DataFrame, returning a new object (a copy) with the new columns added to the original ones. Existing columns that are re-assigned will be overwritten
## kwargs : keywords are the column names.
## https://www.geeksforgeeks.org/pandas-dataframe-assign/


import numpy as np 
arr = np.array([1, 2, 3, 4, 5]) 
arr.assign([6, 7, 8, 9, 10]) 




# TODO: count the no. of non-NA/null
df.count()
DataFrame.count(axis=0, level=None, numeric_only=False)

# axis : 0 or ‘index’ for row-wise, 1 or ‘columns’ for column-wise
# level : If the axis is a MultiIndex (hierarchical), count along a particular level, collapsing into a DataFrame
# numeric_only : Include only float, int, boolean data

#https://www.geeksforgeeks.org/python-pandas-dataframe-count/?ref=previous_article


# i.e.
import pandas as pd 
  
# Creating a dataframe using dictionary 
df = pd.DataFrame({"A":[-5, 8, 12, None, 5, 3],  
                   "B":[-1, None, 6, 4, None, 3], 
                   "C:["sam", "haris", "alex", np.nan, "peter", "nathan"]
                   })
df.count(axis = 0)  # axis = 0 indicates row 

