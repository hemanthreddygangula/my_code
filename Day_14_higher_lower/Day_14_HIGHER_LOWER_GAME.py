import random
import os
import higher_lower_asciiart as pics
import higher_lower_data as dataset
os.system('cls')
print(pics.logo)
count = 0
a = random.randint(0,len(dataset.data))
A = dataset.data[a]
while 1:
    print(f"Your current score is {count}")
    b = random.randint(0,len(dataset.data))
    B = dataset.data[b]
    if A==B:
        b = random.randint(0,len(dataset.data))
        B = dataset.data[b] 
        
    print(f"Compare A: {A['name']}, {A['description']}, {A['country']} ")
    print(f"Compare B: {B['name']}, {B['description']}, {B['country']} ")
    choice = input("Who has more followers. Type 'A' or 'B': ")

    if A['follower_count'] > B['follower_count']:
        high = 'A'
    else:
        high = 'B'

    if choice == high:
        count+=1
        A = B
        print()
    else:
        print("You gussed wrong.")
        print(f"Your Final Score is {count}")
        break