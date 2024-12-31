print("Welcome to the tip calculator !\n")

# Get user inputs and convert them to appropriate types
bill = float(input("What was the total bill ?: "))
tip_amount = float(input("How much percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many persons do you want to split the bill ?: "))

# Calculate the tip percentage
tip_percentage = tip_amount / 100

# Calculate the final tip amount and new bill amount
final_tip = bill * tip_percentage
new_bill = bill + final_tip

# Calculate the amount each person needs to pay
split = new_bill / people

# Print the results
print(f"Your tip is ${final_tip:.2f}, your total bill now is ${new_bill:.2f} and your individual bills are ${split:.2f} per person")
