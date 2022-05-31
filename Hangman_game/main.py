# 🚨 Hangman game Project 👇
import random

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

print("Welcome to the game of Hangman!")
lives = 6
blank_list = []
import hangman_words
chosen_word = random.choice(hangman_words.word_list)
import hangman_art
print(hangman_art.logo)
for k in range(len(chosen_word)):
    blank_list.append("_")

while listToString(blank_list) != chosen_word and lives > 0:
    guess = input("Guess a letter: ").lower()
    for k in range(0, len(chosen_word)):
        if blank_list[k-1] == guess:
            print(f"You already guessed this letter: {guess}")
            break
        elif guess == chosen_word[k-1]:
            blank_list[k-1] = guess
    if guess not in chosen_word:
      lives -= 1
      print(f"letter {guess} is not in the chosen word you loose one live!")
      print(f"Your remain lives: {lives}")
      print(hangman_art.stages[lives-1])
      print(f"{' '.join(blank_list)}")
    else:
      print(f"{' '.join(blank_list)}")
if listToString(blank_list) == chosen_word:
  print("You win!")
else:
  print("You loose!")