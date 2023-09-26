import random

guess = input("Pick A Number Between 1 And 10: ")

number = range(10)

random = random.choice(number)

if random == guess:
    print("You Got It Correct!")
else:
    print(f"You Got It Incorrect\nThe Number Was: {random}")