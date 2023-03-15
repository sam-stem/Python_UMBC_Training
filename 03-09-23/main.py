### Setup Section ###

# We'll learn about how this line of code works later in the course - for now just know it loads the colored text
from colorama import Fore, Back, Style


# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace=False):

  # If it's not in the word, display it with a red background
  if (not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if (isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")


# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if (letter in actual):

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if (letter == actual[index]):  #secret[position]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:
        printColorfulLetter(letter, True, False)

      # ...so we'll print it out with a yellow background

    # ...but if the letter is not in the word at all...
    else:
      printColorfulLetter(letter, False, False)
    # ...print it out with a red background

    # Don't worry about the line of code below, it works. It just handles the transition between colors
    print(Style.RESET_ALL + " ", end="")


# TO-DO: Write a Function that takes in a six-lettered word from the user


def wordPrompt(length):
  #prompt the user for input
  prompt = input(f"\nPlease enter a {length} character word: \n")
  #error handling prompt the user until the right length
  while (len(prompt) != length):
    prompt = input(f"\nSorry, please enter a {length} character word: \n")
  return prompt


# This marks the end of the function definitions, below this is where the program will actually start!

### Main Program ###
actual = "sample"
length = len(actual)
attempts = wordPrompt(length)
index = 0
attemptsCount = 6
while (index < attemptsCount and attempts != actual):
  printGuessAccuracy(attempts, actual)
  attempts = wordPrompt(length)
  #for i in range(attemptsCount):
  print("\n")
  index += 1

if (attempts == actual):
  printGuessAccuracy(attempts, actual)
  print(
    "\nCongralutations that is the correct word and you won within the number of attempts "
  )
else:
  print(f"\nYou have run out of attempts. You lose!")

#if(len(attempts) == 6):
# printGuessAccuracy(attempts, actual)
# elif(len(attempts) != 6):
# attempts = input("Sorry, Please enter a six character word: ")
# else:
# attempts = input("Sorry, Please enter a six character word: ")
# TO-DO: Write the logic of the game here!
