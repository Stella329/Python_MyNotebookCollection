from art import logo
print(logo)
import random 

###FUN
#user picks an answ: 函数
def guess():
  guess_raw = input('Make a guess: ')  ## string->
  
  ## check if a string input is a number
  ## method 1: using   except ValueError
  ## method 2: using   if userinput.isnumeric(); or isdecimal(), or isdigit()
  while guess_raw.isdecimal() == False:
      print('Invalid Input, please guess again.\n')
      guess_raw = input('Make a guess: ')
  guess = int(guess_raw)
  return guess

def play_again():
  play_again = input('\nWhat to play again? Type "y" or "n": ').lower()
  if play_again == 'n':
    return False
  else:
    return True

###BODY
#Continue: 游戏重复开始判定!!
if_continue = True
while if_continue==True:
  
  #comp pick an answ：
  ans = random. randint(1, 100) #randint includes both sides!!
  print('\nI\'m thinking about a number (an integer) between 1 and 100.')
  #print(f'test_code answ={ans}') ## test code
  
  #game level
  level = 'none'
  while level!='easy' and level!='hard':
    level = input('\nChoose a level for the game: type "hard" or "easy": ').lower()
    if level == 'hard':
      lives = 5
      print('You\'ll have 5 attempts.')
    elif level == 'easy':
      lives = 10
      print('You\'ll have 10 attempts.')
    else:
      print('Invaild type-in. Please choose "hard" or "easy" again: ')
      level = 'none'
      
  
  
  #Compare: 游戏输赢判定！！！  
  while if_continue == True:
    if lives == 0: #判定: 是否可以继续？
      if_continue = False
      print('You are running out of lives. You lose.😢')

      
    else: 
      #user picks an answ:
      user_guess = guess() 
      
      if user_guess == ans:
        if_continue = False
        print(f'Bingo!!! {ans} is the number!! You guessed right!!🎈🎈🎈')
      
      elif user_guess > ans:
        print('It\'s too high.')
        lives -= 1
      
      else:
        print('It\'s too small.')
        lives -= 1

  if_continue = play_again()
  if if_continue == False:
    print('\nGoodbye! 👹')