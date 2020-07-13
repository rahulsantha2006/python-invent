import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
  =======''', '''
  
  +---+
  |   |
  O   |
      |
      |
      |
  =======''', '''
  
  +---+
  |   |
  O   |
  |   |
      |
      |
  =======''', '''
  
  +---+
  |   |
  O   |
 /|   |
      |
      |
 ========''', '''
 
 +---+
 |   |
 O   |
/|\  |
     |
     |
 ========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
 =======''', '''
 
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
 =======''']

sentence = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion
lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon
python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake
spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat
zebra'''
words = sentence.split()

def getRandomWord(wordlist):
    wordIndex = random.randint(0, len(wordlist) - 1)
    return wordlist[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    # this for loop will print the letters you have missed
    print('Missed Letters:', end='')
    for letter in missedLetters:
        print(letter, end='')
    print()
    # this for loop identifies the characters in the secret word and makes blanks accordingly
    # it will also replace any of the correctly guessed letters to the relating space
    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):

        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
    # prints the secret word with spaces between each letter letter
    for letter in blanks:
        print(letter, end='')
    print()


# Makes sure the player enters a valid character as a input
def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

# Start of the program ==================================================
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    #   lets the player type a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is ' + secretWord + '! You have won')

            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

            print('You have run out of guesses!\nAfter' + str(len(missedLetters)) +
                  'missed guesses and' + str(len(correctLetters)) + ' correct guesses, the word was'
                  + secretWord + '')
            gameIsDone = True

        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break
