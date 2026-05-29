"""
WEEK 1 PROJECT: Calculator App
A simple calculator that performs basic arithmetic operations

Features:
- Addition, Subtraction, Multiplication, Division
- Modulus and Exponentiation
- Error handling
- Menu-driven interface
"""

def display_menu():
    """Display calculator menu"""
    print("\n" + "=" * 50)
    print("         🧮 SIMPLE CALCULATOR 🧮")
    print("=" * 50)
    print("Available Operations:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (×)")
    print("  4. Division (÷)")
    print("  5. Modulus (%)")
    print("  6. Exponentiation (^)")
    print("  0. Exit")
    print("=" * 50)


def add(a, b):
    """Addition function"""
    return a + b


def subtract(a, b):
    """Subtraction function"""
    return a - b


def multiply(a, b):
    """Multiplication function"""
    return a * b


def divide(a, b):
    """Division function with error handling"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def modulus(a, b):
    """Modulus function"""
    if b == 0:
        return "Error: Cannot perform modulus with zero!"
    return a % b


def power(a, b):
    """Exponentiation function"""
    return a ** b


def get_number(prompt):
    """Get number input from user with validation"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def calculator():
    """Main calculator function"""
    print("\n🎉 Welcome to Simple Calculator!")
    
    while True:
        display_menu()
        
        # Get operation choice
        choice = input("\nEnter your choice (0-6): ")
        
        # Exit condition
        if choice == '0':
            print("\n👋 Thank you for using Calculator!")
            print("Goodbye! 🎉\n")
            break
        
        # Validate choice
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("\n❌ Invalid choice! Please select 0-6.")
            input("Press Enter to continue...")
            continue
        
        # Get numbers from user
        print()
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        # Perform operation based on choice
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
            
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
            
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "×"
            
        elif choice == '4':
            result = divide(num1, num2)
            operation = "÷"
            
        elif choice == '5':
            result = modulus(num1, num2)
            operation = "%"
            
        elif choice == '6':
            result = power(num1, num2)
            operation = "^"
        
        # Display result
        print("\n" + "-" * 50)
        if isinstance(result, str):  # Error message
            print(f"  {result}")
        else:
            # Format numbers for display
            if num1 == int(num1):
                num1 = int(num1)
            if num2 == int(num2):
                num2 = int(num2)
            if isinstance(result, float) and result == int(result):
                result = int(result)
            
            print(f"  📊 {num1} {operation} {num2} = {result}")
        print("-" * 50)
        
        input("\nPress Enter to continue...")


# ============================================
# STANDALONE FUNCTION DEMONSTRATIONS
# ============================================
def demo_calculator_functions():
    """Demonstrate calculator functions without user input"""
    print("\n" + "=" * 50)
    print("CALCULATOR FUNCTIONS DEMO")
    print("=" * 50)
    
    # Test values
    a, b = 10, 3
    
    print(f"\nTest values: a = {a}, b = {b}\n")
    
    print(f"Addition       : {a} + {b} = {add(a, b)}")
    print(f"Subtraction    : {a} - {b} = {subtract(a, b)}")
    print(f"Multiplication : {a} × {b} = {multiply(a, b)}")
    print(f"Division       : {a} ÷ {b} = {divide(a, b):.2f}")
    print(f"Modulus        : {a} % {b} = {modulus(a, b)}")
    print(f"Exponentiation : {a} ^ {b} = {power(a, b)}")
    
    # Test with different values
    print(f"\nTest values: a = 20, b = 4\n")
    a, b = 20, 4
    
    print(f"Addition       : {a} + {b} = {add(a, b)}")
    print(f"Subtraction    : {a} - {b} = {subtract(a, b)}")
    print(f"Multiplication : {a} × {b} = {multiply(a, b)}")
    print(f"Division       : {a} ÷ {b} = {divide(a, b)}")
    print(f"Modulus        : {a} % {b} = {modulus(a, b)}")
    print(f"Exponentiation : {a} ^ {b} = {power(a, b)}")
    
    # Test error cases
    print(f"\nError handling test:")
    print(f"Division by zero   : 10 ÷ 0 = {divide(10, 0)}")
    print(f"Modulus with zero  : 10 % 0 = {modulus(10, 0)}")
    
    print("\n" + "=" * 50)


# ============================================
# MAIN PROGRAM
# ============================================
if __name__ == "__main__":
    # First, show demo of all functions
    demo_calculator_functions()
    
    # Ask user if they want to use interactive calculator
    print("\n" + "=" * 50)
    print("INTERACTIVE CALCULATOR")
    print("=" * 50)
    print("\nThe interactive calculator requires user input.")
    print("Uncomment the line below to run it:\n")
    print("    # calculator()")
    print("\nOr run this file and type 'calculator()' in the Python shell.")
    print("=" * 50)
    
    # Uncomment the line below to run interactive calculator
    # calculator()
    
    # Alternative: Run with a simple yes/no prompt
    print("\n")
    response = input("Do you want to run the interactive calculator? (yes/no): ").lower()
    if response in ['yes', 'y']:
        calculator()
    else:
        print("\n✅ Demo completed! Run calculator() to try the interactive version.")
