import json
from datetime import datetime

# ==============================
# 1. Input Validation Class
# Handles safe type casting from user input
# ==============================
class InputValidator:
    @staticmethod
    def get_float_input(prompt: str) -> float:
        """Safely get float input from user with validation"""
        while True:
            try:
                value = float(input(prompt))  # Cast string to float
                return value
            except ValueError:
                print("Invalid input. Please enter a number!")

    @staticmethod
    def get_int_input(prompt: str) -> int:
        """Safely get integer input from user with validation"""
        while True:
            try:
                value = int(input(prompt))  # Cast string to integer
                return value
            except ValueError:
                print("Invalid input. Please enter an integer!")

# ==============================
# 2. Financial Calculator Class
# Core financial calculations with type casting
# ==============================
class FinancialCalculator:
    def __init__(self):
        # Using list to store calculation history
        self.history = []

    def simple_interest(self, principal: float, rate: float, time: float) -> float:
        """Calculate simple interest: I = P * R * T / 100"""
        return principal * rate * time / 100

    def compound_interest(self, principal: float, rate: float, time: float, frequency: int) -> float:
        """Calculate compound interest: A = P(1 + r/n)^(nt)"""
        return principal * (1 + rate/(frequency * 100))**(frequency * time) - principal

    def currency_converter(self, amount: float, rate: float) -> float:
        """Convert currency: amount * rate"""
        return amount * rate

    def add_to_history(self, calculation_type: str, result: float):
        """Add calculation to history with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append({
            "timestamp": timestamp,
            "type": calculation_type,
            "result": result
        })

# ==============================
# 3. History Management Class
# Handles saving/loading history to/from JSON
# ==============================
class HistoryManager:
    def __init__(self, calculator: FinancialCalculator):
        self.calculator = calculator

    def save_history(self, filename: str = "history.json"):
        """Save calculation history to JSON file"""
        with open(filename, "w") as f:
            # Serialize Python object to JSON string
            json.dump(self.calculator.history, f, indent=2)

    def load_history(self, filename: str = "history.json"):
        """Load calculation history from JSON file"""
        try:
            with open(filename, "r") as f:
                # Deserialize JSON string to Python object
                loaded = json.load(f)
                self.calculator.history = loaded
                print(f"Successfully loaded {len(loaded)} history entries.")
        except FileNotFoundError:
            print("No previous history found.")

# ==============================
# 4. Utility Functions
# Formatting and parsing utilities for currency values
# ==============================
def format_currency(value: float, currency: str = "$") -> str:
    """Format float as currency string with thousand separators"""
    return f"{currency}{value:,.2f}"  # Cast float to formatted string

def parse_currency_string(value: str) -> float:
    """Parse currency string back to float value"""
    # Remove currency symbol and thousand separators before casting
    return float(value.replace("$", "").replace(",", ""))

# ==============================
# 5. Main Program
# User interface and control flow
# ==============================
def main():
    print("=== Financial Calculator with Dynamic Type Casting ===")
    
    # Initialize objects
    calculator = FinancialCalculator()
    history_manager = HistoryManager(calculator)
    history_manager.load_history()

    while True:
        print("\n=== Main Menu ===")
        print("1. Simple Interest Calculation")
        print("2. Compound Interest Calculation")
        print("3. Currency Conversion")
        print("4. View Calculation History")
        print("5. Save & Exit")
        
        choice = input("Select operation (1-5): ")

        if choice == "1":
            print("\n=== Simple Interest Calculator ===")
            # Get inputs with automatic type casting
            principal = InputValidator.get_float_input("Enter principal amount: ")
            rate = InputValidator.get_float_input("Enter interest rate (% per year): ")
            time = InputValidator.get_float_input("Enter time (years): ")
            
            # Perform calculation
            result = calculator.simple_interest(principal, rate, time)
            print(f"Simple Interest: {format_currency(result)}")
            calculator.add_to_history("Simple Interest", result)

        elif choice == "2":
            print("\n=== Compound Interest Calculator ===")
            principal = InputValidator.get_float_input("Enter principal amount: ")
            rate = InputValidator.get_float_input("Enter interest rate (% per year): ")
            time = InputValidator.get_float_input("Enter time (years): ")
            frequency = InputValidator.get_int_input("Interest compounding frequency per year: ")
            
            result = calculator.compound_interest(principal, rate, time, frequency)
            print(f"Compound Interest: {format_currency(result)}")
            calculator.add_to_history("Compound Interest", result)

        elif choice == "3":
            print("\n=== Currency Converter ===")
            amount = InputValidator.get_float_input("Enter amount: ")
            rate = InputValidator.get_float_input("Enter exchange rate: ")
            
            result = calculator.currency_converter(amount, rate)
            print(f"Converted amount: {format_currency(result)}")
            calculator.add_to_history("Currency Conversion", result)

        elif choice == "4":
            print("\n=== Calculation History ===")
            if not calculator.history:
                print("No calculation history available.")
            else:
                # Show last 5 entries
                for entry in calculator.history[-5:]:
                    print(f"{entry['timestamp']} | {entry['type']} | {format_currency(entry['result'])}")

        elif choice == "5":
            history_manager.save_history()
            print("History saved. Thank you!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()