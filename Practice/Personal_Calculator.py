# Import math module for calculations
import math

# 1. BMI Calculator
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# 2. Expense Tracker
def track_expenses():
    expenses = []
    print("\n=== Daily Expense Tracker ===")
    while True:
        try:
            amount = float(input("Enter expense amount (0 to finish): "))
            if amount == 0:
                break
            expenses.append(amount)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return sum(expenses)

# 3. Savings Calculator
def calculate_daily_savings(salary, savings_goal_percent):
    monthly_savings = salary * (savings_goal_percent / 100)
    return monthly_savings / 30  # Average daily savings

# 4. Main Menu
def main():
    print("=== Personal Finance & Health Manager ===")
    
    # User input
    name = input("Enter your name: ")
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    salary = float(input("Enter your monthly salary: "))
    savings_goal = float(input("Enter your savings goal (%) per month: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    
    # Calculate savings
    daily_savings = calculate_daily_savings(salary, savings_goal)
    
    # Track expenses
    total_expenses = track_expenses()
    
    # Daily Summary
    print("\n=== Daily Summary ===")
    print(f"Name: {name}")
    print(f"BMI: {bmi:.2f} ({category})")
    print(f"Total Expenses Today: ${total_expenses:.2f}")
    print(f"Daily Savings Target: ${daily_savings:.2f}")
    print(f"Remaining Balance: ${salary/30 - total_expenses:.2f}")

# Run the program
if __name__ == "__main__":
    main()