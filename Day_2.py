print("Welcome to Tip Calculator")
bill = float(input("What was the total Bill? $"))
tip_percent = float(input("What percent tip would you like to give? "))
no_of_people = int(input("No. of people will split the bill? "))

pay = round(((bill + bill*(tip_percent/100)) /no_of_people), 2)
print(f"Each person should pay ${pay}")