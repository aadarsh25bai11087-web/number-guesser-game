import random

print("Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
print()

play = "yes"

while play == "yes" or play == "y":
    num = random.randint(1, 100)
    tries = 0
    guessed = False
    
    while guessed == False:
        guess = int(input("Enter your guess: "))
        tries = tries + 1
        
        if guess < num:
            print("Too low! Try again")
            print()
        elif guess > num:
            print("Too high! Try again")
            print()
        else:
            guessed = True
            print("Congratulations! You got it!")
            print("You took", tries, "attempts")
            print()
    
    play = input("Do you want to play again? (yes/no): ")
    print()
    if play == "yes" or play == "y":
        print("Great! Let's play again")
        print()

print("Thanks for playing!")
