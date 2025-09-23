# Step 1 - Welcome the user with a message 'Welcome to the Tip Calculator'
# Step 2 - Ask what the total bill was and save as total_bill
# Step 3 - Ask what percentage tip the user would like to give, 10, 12 or 15 and save as tip_percentage
# Step 4 - Ask how many people the bill should be split between and store as total_diners
# Step 5 - Let the user know that 'Each person should pay: $x'

print("Welcome to the Tip Calculator!\n")
bill = float(input("What is the total of the bill? \n$"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? \n"))
total_diners = int(input("Between how many diners should the total bill be split? \n"))
bill_plus_tip = bill + (bill * (tip_percentage / 100))
bill_per_person = bill_plus_tip / total_diners

print(f"Each person should pay: ${bill_per_person:.2f}")

