import random
import time

def displayIntro():
    print('you are in a land full of dragons, in front of you you see 2 caves')
    print('one cave has a dragon that is friendly, and the other is not so much')
    print()

def chooseCave():
    cave=''
    while cave !='1' and cave !='2':
        print('Which cave are you choosing to go in, 1 or 2')
        cave=input()

    return cave

def checkCave(chosenCave):
        print('you approach the cave...')
        time.sleep(2)
        print('It is dark and spooky...')
        time.sleep(2)
        print('A large dragon jumps in front of you and opens his mouth and...')
        print()
        time.sleep(2)

        friendlyCave= random.randint(1,2)

        if chosenCave == str(friendlyCave):
            print('Gives you his treasure')

        else:
            print('gobbles you down in 1 bite')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Do you want to play again?(yes or no)')

    playAgain = input()