
#List Comprehension: Looping through list
new_list  = [ new_item for item in list ] 


#Dict Comprehension:
#Looping through an sequences
new_dic = {new_key: new_value for item in sequence if test}
#Looping through an dict
new_dic = {new_key: new_value for (key, value) in dict.items()}  


#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass


#———————————————START OF THE I.E.———————————————#

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
{new_key:new_value for (index, row) in df.iterrows()}





#———————————————OLD VERSION OF NATO ALPHABETS———————————————#

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_df = pandas.read_csv('nato_phonetic_alphabet.csv')  
nato_dict ={row.letter : row.code for (index,row) in nato_df.iterrows()} ##df.iterrows()


##NB: 如果nato_dict = nato_df.to_dict() -->只返回column values, by column names
## { column_name_1: {column_value1, 2, 3,...}, column_name_2: {value1,2,3...} }




#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = list(input('Enter a word: ').upper())
decode_dic = {letter: nato_dict[letter] for letter in user_input}
## return: {'S': 'Sierra', 'T': 'Tango', 'E': 'Echo', 'L': 'Lima', 'A': 'Alfa'}

for key in decode_dic:   ##只能loop through dict_key
    print(f'{key} : {decode_dic[key]}')


# METHOD 2
user_input = input('Enter a word: ').upper()
output_list = [nato_dict[letter] for letter in user_input]
print(output_list)

