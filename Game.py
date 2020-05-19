import random
import time

# intro
print("Welcome! Let's go playyyy!")
list_of_choices = ["Rock", "Paper", "Scissors"]
print("You can either choose 1. Rock, 2.Paper or 3. Scissors ")
turns = 3

while turns < 4:
    choice_1 = input("1,2 or 3?")
    if choice_1 == list_of_choices[0]: