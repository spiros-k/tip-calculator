print("Welcome to the tip calculatr!")

total_bill = input("How much is the total bill?\n €")
tip_percentage = input("How much tip do you want to give? 7, 10, 12, or 15?\n")
people = input("How many people have to pay for the bill?\n")

bill_per_person = float(total_bill) / int(people)
bill_with_tip_per_person = float(bill_per_person) + (float(bill_per_person) * (int(tip_percentage) / 100)) 

print(f"Each person has to pay: {round(bill_with_tip_per_person, 2)}€")