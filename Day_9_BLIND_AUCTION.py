import os

d = {}
def auction(name,bid):
    d[name] = bid
    return d
while 1:
    os.system('cls')
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    listt = auction(name,bid) 
    a = input("Type Yes if there are any bidders else No") 
    if a=='no' or 'No':
        break
print(listt)
maxx = max(listt.values())
keys = list(listt.keys())
values = list(listt.values())
pos = values.index(maxx)
print(f"The winner of the auction is {keys[pos]} and the bid is {maxx}")