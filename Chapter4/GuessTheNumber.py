import random

guessesTaken = 0
guessLimit = 10

print(" Hello, What is you name?")
name = input()

number = random.randint(1, 20)
print(name + " i am thinking of a number between 1 and 20; You have ", guessLimit, " guesses!!")

while guessesTaken < guessLimit:
    print("Take a guess")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("your number is too low")

    if guess > number:
        print("your number is too high")

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Great work ' + name + ' You guessed the number in ' + guessesTaken + ' guesses')
        break

# loop ended here

if guessesTaken == guessLimit:
    number = str(number)
    print("No, the number i was thinking of is " + number)
