from guess_number_art import logo
import random

print(logo)
print("             Welcome to the Number Guessing Game!".upper())
print()
print("I'm thinking of a number between 1 and 100")
number = random.randint(0,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "hard":
    life = 5
else:
    life = 10

end = True
while end:
    print(f"You have {life} attempts remaining to guess the number.")
    guess = int(input("Make a guess:"))
    if guess < number:
        print("Too low.")
        print("Guess again.")
        life -= 1
    elif guess > number:
        print("Too high.")
        print("Guess again.")
        life -= 1
    else:
        print(f"You got the right number, the answer is: {number}")
        end = False
    if life == 0:
        print("You've run out of guesses, you lose.")
        end = False



