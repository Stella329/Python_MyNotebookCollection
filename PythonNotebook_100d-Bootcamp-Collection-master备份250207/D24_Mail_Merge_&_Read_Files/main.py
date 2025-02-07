#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = '[name]'

with open('./Input/Names/invited_names.txt',mode='r') as name_file:
    names = name_file.readlines() ##currently print: ['Aang\n', 'Zuko\n', ...]



with open('./Input/Letters/starting_letter.txt', mode='r') as letter_file:
    letter = letter_file.read()

    for item in names:  ## Aang/n
        stripped_item = item.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_item)
        print(new_letter)

        ##todo: save the new_letter
        ##if open a non-existing file, python will create a new file for it.
        with open(f'./Output/ReadyToSend/Letter_to_{stripped_item}.txt', mode='w') as completed_letter: ## currently empty
            completed_letter.write(new_letter)


# ----------OPEN AND WRITE A FILE-------------------
# OPEN AND READ
## METHODS 1: manually close
    f = open("demofile3.txt", "r")
    f.write("Woops! I have deleted the content!")
    f.close()


## METHOD 2: auto close
with open ('file_name.txt') as file:
    file.read()


# ----------OTHER METHODS-------------------
# READLINES
## readline(): Return all lines in the file, as a [list] where each line is an item in the list object:
## f = open("demofile.txt", "r")
## Print(f.readlines(33))

## REPLACE()
## string.replace(oldvalue, newvalue, count)
## txt = "I like bananas"
## x = txt.replace("bananas", "apples")

## STRIP()
## The strip() method removes any leading, and trailing whitespaces. Leading means at the beginning of the string, trailing means at the end.但保留中间空格，不会对正文造成影响
## string.strip(characters)
## txt = ",,,,,rrttgg.....banana....rrr"
## x = txt.strip(",.grt")
## -- print: banana


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp