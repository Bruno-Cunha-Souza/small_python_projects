from converter import UnitConverter

def display_menu():
    print("\n============================")
    print("        Unit Converter")
    print("============================\n")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    print("3. Liters to Gallons")
    print("4. Gallons to Liters")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. Celsius to Fahrenheit")
    print("8. Fahrenheit to Celsius")
    print("9. Exit")

def menu():
    converter = UnitConverter()

    while True:
        display_menu()
        
        choice = input("\nChoose an option: ")
        
        if choice not in [str(i) for i in range(1, 10)]:
            print("\nInvalid option. Try again.")
            continue
        
        if choice == '9':
            print("Leaving...")
            break
        
        try:
            value = float(input("\nEnter the value to be converted: "))
        except ValueError:
            print("\nInvalid input. Please enter a numeric value.")
            continue
        
        match choice:
            case '1':
                print(f'\n{value} meters are {converter.convert(value, "meters", "feet")} feet.')
            case '2':
                print(f'\n{value} feet are {converter.convert(value, "feet", "meters")} meters.')
            case '3':
                print(f'\n{value} liters are {converter.convert(value, "liters", "gallons")} gallons.')
            case '4':
                print(f'\n{value} gallons are {converter.convert(value, "gallons", "liters")} liters.')
            case '5':
                print(f'\n{value} kilograms are {converter.convert(value, "kilograms", "pounds")} pounds.')
            case '6':
                print(f'\n{value} pounds are {converter.convert(value, "pounds", "kilograms")} kilograms.')
            case '7':
                print(f'\n{value} celsius are {converter.convert(value, "celsius", "fahrenheit")} fahrenheit.')
            case '8':
                print(f'\n{value} fahrenheit are {converter.convert(value, "fahrenheit", "celsius")} celsius.')
        
        print()