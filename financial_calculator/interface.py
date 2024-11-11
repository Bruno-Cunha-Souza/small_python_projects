from calculations import calculate_simple_interest, calculate_compound_interest, calculate_present_value, calculate_future_value
from utils import get_float_input, get_int_input

def menu():
    while True:
        print("\n============================")
        print("   Financial Calculator")
        print("============================\n")
        print("1. Calculate Simple Interest")
        print("2. Calculate Compound Interest")
        print("3. Calculate Present Value")
        print("4. Calculate Future Value")
        print("5. Exit")
        
        choice = get_int_input("\nChoose an option: ")
        
        match choice:
            case 1:
                calculate_simple_interest_ui()
            case 2:
                calculate_compound_interest_ui()
            case 3:
                calculate_present_value_ui()
            case 4:
                calculate_future_value_ui()
            case 5:
                print("\nLeaving...")
                break
            case _:
                print("\nInvalid option. Please choose again.")

def calculate_simple_interest_ui():
    principal = get_float_input("\nEnter the main amount: ")
    rate = get_float_input("Enter the interest rate (in decimal): ")
    time = get_float_input("Enter time (in years): ")
    result = calculate_simple_interest(principal, rate, time)
    print(f"The amount with simple interest is: {result}")

def calculate_compound_interest_ui():
    principal = get_float_input("\nEnter the main amount: ")
    rate = get_float_input("Enter the interest rate (in decimal): ")
    time = get_float_input("Enter time (in years): ")
    n = get_int_input("Enter the number of compositions per year: ")
    result = calculate_compound_interest(principal, rate, time, n)
    print(f"The amount with compound interest is: {result}")

def calculate_present_value_ui():
    future_value = get_float_input("\nEnter the future value: ")
    rate = get_float_input("Enter the interest rate (in decimal): ")
    time = get_float_input("Enter time (in years): ")
    result = calculate_present_value(future_value, rate, time)
    print(f"The present value is: {result}")

def calculate_future_value_ui():
    present_value = get_float_input("\nEnter the present value: ")
    rate = get_float_input("Enter the interest rate (in decimal): ")
    time = get_float_input("Enter time (in years): ")
    result = calculate_future_value(present_value, rate, time)
    print(f"The future value is: {result}")
