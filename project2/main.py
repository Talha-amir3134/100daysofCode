print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill? $"))
tipPct = float(input("How much tip would you like to give? 10, 12 or 15? "))
totalPeople = float(input("How many people to split the bill? "))
tipAmount = totalBill * tipPct / 100
totalBill += tipAmount
individualBill = totalBill / (totalPeople)
print(f'Each person should pay: ${individualBill:.2f}')