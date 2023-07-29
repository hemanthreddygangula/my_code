import os
water = 500
powder = 200
milk = 300

cost_expresso = 1.50
cost_latte = 2.50
cost_cappucino = 3.00

def expresso():
    global water, milk, powder
    m = 0
    w = 15
    p = 18
    
    water-=w
    milk-=m
    powder-=p

    if water<0:
        print("Water is insufficient.\nPlease turn off machine and refill the resources")
        return 0
    if milk<0:
        print("Milk is insufficient.\nPlease turn off machine and refill the resources")
        return 0
    if powder<0:
        print("Coffee powder is insufficient.\nPlease turn off machine and refill the resources")
        return 0

def latte():
    global water, milk, powder
    m = 150
    w = 200
    p = 24

    water-=w
    milk-=m
    powder-=p
    
    if water<0:
        print("Water is insufficient.\nPlease turn off machine and refill the resources")
        return 0
    if milk<0:
        print("Milk is insufficient.\nPlease turn off machine and refill the resources")
        return 0
    if powder<0:
        print("Coffee powder is insufficient.\nPlease turn off machine and refill the resources")
        return 0

def cappuccino():
    global water, milk, powder
    m = 100
    w = 250
    p = 24

    water-=w
    milk-=m
    powder-=p
    
    if water<0:
        print("Water is insufficient.\nPlease turn off machine and refill the resources")
        return 0
    if milk<0:
        print("Milk is insufficient.\nPlease turn off machine and refill the resources")
        return 0
    if powder<0:
        print("Coffee powder is insufficient.\nPlease turn off machine and refill the resources")
        return 0

def main():
    os.system('cls')
    switch = input("Coffee machine is currently off. Please enter 'on' to turn on the machine: ")
    if switch == 'on' or switch == 'On' or switch == 'ON':
        coffee = 'on'
        while coffee!='off':
            global water, milk, powder
            coffee = input("\nMENU.\nChoose 1 for expresso\nChoose 2 for latte\nChoose 3 for cappuccino\nwhat do you want: ")
            flag = 0
            if coffee == '1':
                flag = expresso()
            elif coffee == '2':
                flag = latte()
            elif coffee == '3':
                flag = cappuccino()
            global cost_expresso, cost_cappucino, cost_latte
            if flag != 0:
                print("Please enter coins in machine")
                quaters = int(input("No. of quarters: "))*0.25
                dime = int(input("No. of dimes: "))*0.10
                penny = int(input("No. of penny: "))*0.01
                nickel = int(input("No.of nickels: "))*0.05
                amt = quaters+dime+penny+nickel
                if coffee == '1':
                    if amt>cost_expresso:
                        print(f"Here's your change ${amt-cost_expresso}")
                        print("\nEnjoy your coffee\n")
                    elif amt<cost_expresso:
                        print("Insufficient money. Money refunded!")
                    else:
                        print()
                elif coffee == '2':
                    if amt>cost_latte:
                        print(f"Here's your change ${amt-cost_latte}")
                        print("\nEnjoy your coffee\n")
                    elif amt<cost_latte:
                        print("Insufficient money. Money refunded!")
                    else:
                        print()
                elif coffee == '3':
                    if amt>cost_cappucino:
                        print(f"Here's your change ${amt-cost_cappucino}")
                        print("\nEnjoy your coffee\n")
                    elif amt<cost_cappucino:
                        print("Insufficient money. Money refunded!")
                    else:
                        print()
                print("------------------")
main()