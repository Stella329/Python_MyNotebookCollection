import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
import hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
import hangman_art
print(hangman_art.logo)
#print(f'Pssst, the solution is {chosen_word}.') #Testing code

display = [] #Create blanks
for _ in range(word_length):
    display += "_"

history=[] 
    #储存猜过的letter;引入空集放在while loop外（不然会盖）；添加行为放在最后
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know. 难：1.对比两轮的同命变量？2.不掉命？
    if guess in history:
      print(f"\nThe letter '{guess}' is what you've already guessed.")
    else:
      #Check guessed letter
      for position in range(word_length): #chosen word
          letter = chosen_word[position]
          # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}") #test code
          if letter == guess:
              display[position] = letter
  
      #Check if user is wrong.
      if guess not in chosen_word:
          #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
          print(f"\nLetter '{guess}' is not in the word. Your guess is wrong.\n")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print("You lose.")
  
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    stage = hangman_art.stages[lives]
    print(stage)

    history.append(guess)
