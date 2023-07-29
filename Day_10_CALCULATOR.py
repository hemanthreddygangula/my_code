import os

def add(n1,n2):
    return int(n1+n2)
def sub(n1,n2):
    return int(n1-n2)
def mul(n1,n2):
    return int(n1*n2)
def div(n1,n2):
    return n1/n2
def mod(n1,n2):
    return n1%n2



d = {}
def calculator():
    n1 = float(input("Enter Number 1: "))
    while 1:
        op = input("Enter any Operator(+, -, *, /, %): ")
        if op == 'c' or op == 'C':
            break
        n2 = float(input("Enter Number 2: "))
        d['+'] = add(n1,n2)
        d['-'] = sub(n1,n2)
        d['*'] = mul(n1,n2)
        d['/'] = div(n1,n2)
        d['%'] = mod(n1,n2)
        result = d[op]
        print(result)
        n1 = result
        print("Enter C or c to start new calculations")
    os.system('cls')
    calculator()

os.system('cls')
calculator()

