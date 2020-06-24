import random
import time


def displayIntro():
    print('you are in a land full of dragons, in front of you you see 2 caves')
    print('one cave has a dragon that is friendly, and the other is not so much')
    print()


def chooseItem():
    print('You have found two items in a backpack a Sword and a Candycane')
    print('pick which one you want (1 or 2)')

    itemChosen = input()
    if itemChosen == '1':
        print('You have found a sword')

    if itemChosen == '2':
        print('You have found a piece of candy')

    return itemChosen


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave are you choosing to go in, 1 or 2')
        cave = input()

    return cave


def checkCave(chosenCave, itemChosen):
    print('you approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps in front of you and opens his mouth and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave) and itemChosen=='1':
        print('Gives you his treasure')
        print('and farts at you for not bringing any candy')

    if chosenCave == str(friendlyCave) and itemChosen=='2':
        print('Gives you his treasure')
        print('and eats the candy happily')

    if chosenCave != str(friendlyCave) and itemChosen=='1':
        print('tries to eat you but you slay the dragon')

    if chosenCave != str(friendlyCave) and itemChosen =='2':
        print('eats you and the candy for dinner')




# This is the start of the program
playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()

    itemChosenResult = chooseItem()

    caveNumber = chooseCave()

    checkCave(caveNumber, itemChosenResult)

    print('Do you want to play again?(yes or no)')

    playAgain = input()
