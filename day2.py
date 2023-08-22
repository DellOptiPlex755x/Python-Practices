# Tip Calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the TIP CALCULATOR.")
print("------------------------------")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

each_pay = round((total_bill / people) * (1 + tip / 100), 2)

print(f"Each person should pay: {each_pay}")