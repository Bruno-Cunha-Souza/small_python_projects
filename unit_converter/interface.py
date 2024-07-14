from converter import UnitConverter

def menu():
    converter = UnitConverter()

    while True:
        print("\n============================")
        print("   Conversor de Unidades")
        print("============================\n")
        print("1. Metros para Pés")
        print("2. Pés para Metros")
        print("3. Litros para Galões")
        print("4. Galões para Litros")
        print("5. Quilogramas para Libras")
        print("6. Libras para Quilogramas")
        print("7. Celsius para Fahrenheit")
        print("8. Fahrenheit para Celsius")
        print("9. Sair")
        
        choice = input("\nEscolha uma opção: ")
        
        if choice == '9':
            print("Saindo...")
            break
        
        value = float(input("\nDigite o valor a ser convertido: "))
        
        if choice == '1':
            print(f'\n{value} metros são {converter.convert(value, "meters", "feet")} pés.')
        elif choice == '2':
            print(f'\n{value} pés são {converter.convert(value, "feet", "meters")} metros.')
        elif choice == '3':
            print(f'\n{value} litros são {converter.convert(value, "liters", "gallons")} galões.')
        elif choice == '4':
            print(f'\n{value} galões são {converter.convert(value, "gallons", "liters")} litros.')
        elif choice == '5':
            print(f'\n{value} quilogramas são {converter.convert(value, "kilograms", "pounds")} libras.')
        elif choice == '6':
            print(f'\n{value} libras são {converter.convert(value, "pounds", "kilograms")} quilogramas.')
        elif choice == '7':
            print(f'\n{value} graus Celsius são {converter.convert(value, "celsius", "fahrenheit")} graus Fahrenheit.')
        elif choice == '8':
            print(f'\n{value} graus Fahrenheit são {converter.convert(value, "fahrenheit", "celsius")} graus Celsius.')
        else:
            print("\nOpção inválida. Tente novamente.")
        
        print()