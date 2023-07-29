import os
import random

def game(number,n):
    for i in range(n):
        choice = int(input())
        if number > choice:
            print("Value is too low")
            print(f"You have {n-i-1} remaining")
        elif number < choice:
            print("Value is too high")
            print(f"You have {n-i-1} remaining")
        elif number == choice:
            print("You gussed the correct number")
            return
    print("Your chances are over")

def main():
    os.system('cls')
    print("welcome to the number gussing game")
    print("Iam thinking of a number between 1 to 100. GUESS IT")
    number = random.randint(1,100)
    difficulty = input("Choose the difficulty. 'easy' or 'hard': ")
    if difficulty == 'easy':
        print("You have 15 chances to guess the number.")
        game(number,15)
    elif difficulty == 'hard':
        print("You have 10 chances to guess the number.")
        game(number,10)

main()
