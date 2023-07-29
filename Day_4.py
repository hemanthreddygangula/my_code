import random
# a = random.random() # for float
# b = random.randint(1,5) # for integer
# print(a)
Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game = [Rock, Paper, Scissors]
c=0
b = [0,1,2]
while c in b:
    print("*"*30)
    print("Lets play ROCK PAPER SCISSORS!")
    c = int(input("Choose 1 for Rock, 2 for paper, 3 for scissors, any other to EXIT: "))
    c -= 1
    if c not in b:
        break

    print(game[c])
    if c==0:
        print("You choose ROCK")
    elif c==1:
        print("You choose PAPER")
    elif c==2:
        print("You choose SCISSORS")


    a = random.randint(0,2)
    print(game[a])
    if a==0:
        print("System choose ROCK")
    elif a==1:
        print("System choose PAPER")
    elif a==2:
        print("System choose SCISSORS")


    if (c==0 and a==1) or (c==1 and a==2) or (c==2 and a==0) :
        print("System wins!")
    elif (a==0 and c==1) or (a==1 and c==2) or (a==2 and c==0):
        print("You win!")
    else:
        print("Its a DRAW")
