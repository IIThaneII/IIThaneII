import higher_lower_art
import higher_lower_data
import random

def rand():
    return random.choice(list(higher_lower_data.data))

print(higher_lower_art.logo)
def compare(c):
    a = c
    b = rand()
    while a == b: #make sure that 2 A & B are distinct
        b = rand()
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(higher_lower_art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
    result = input("Who has more followers? Type 'A' or 'B': ")
    if (result == "A") and (int(a['follower_count']) > int(b['follower_count'])):
        return b
    elif (result == "B") and (int(b['follower_count']) > int(a['follower_count'])):
        return a
    else:
        return "f"
score = 0
re_play = True
c = rand()
while re_play:
    d = compare(c)
    if d != "f":
        c = d
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        re_play = False
