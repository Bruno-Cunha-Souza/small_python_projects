from calculations import calculate_simple_interest, calculate_compound_interest, calculate_present_value, calculate_future_value
from utils import get_float_input, get_int_input

def menu():
    while True:
        print("\n============================")
        print("  Calculadora Financeira")
        print("============================\n")
        print("1. Calcular Juros Simples")
        print("2. Calcular Juros Compostos")
        print("3. Calcular Valor Presente")
        print("4. Calcular Valor Futuro")
        print("5. Sair")
        
        choice = get_int_input("\nEscolha uma opção: ")
        
        if choice == 1:
            calculate_simple_interest_ui()
        elif choice == 2:
            calculate_compound_interest_ui()
        elif choice == 3:
            calculate_present_value_ui()
        elif choice == 4:
            calculate_future_value_ui()
        elif choice == 5:
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida. Por favor, escolha novamente.")

def calculate_simple_interest_ui():
    principal = get_float_input("\nDigite o valor principal: ")
    rate = get_float_input("Digite a taxa de juros (em decimal): ")
    time = get_float_input("Digite o tempo (em anos): ")
    result = calculate_simple_interest(principal, rate, time)
    print(f"O montante com juros simples é: {result}")

def calculate_compound_interest_ui():
    principal = get_float_input("\nDigite o valor principal: ")
    rate = get_float_input("Digite a taxa de juros (em decimal): ")
    time = get_float_input("Digite o tempo (em anos): ")
    n = get_int_input("Digite o número de composições por ano: ")
    result = calculate_compound_interest(principal, rate, time, n)
    print(f"O montante com juros compostos é: {result}")

def calculate_present_value_ui():
    future_value = get_float_input("\nDigite o valor futuro: ")
    rate = get_float_input("Digite a taxa de juros (em decimal): ")
    time = get_float_input("Digite o tempo (em anos): ")
    result = calculate_present_value(future_value, rate, time)
    print(f"O valor presente é: {result}")

def calculate_future_value_ui():
    present_value = get_float_input("\nDigite o valor presente: ")
    rate = get_float_input("Digite a taxa de juros (em decimal): ")
    time = get_float_input("Digite o tempo (em anos): ")
    result = calculate_future_value(present_value, rate, time)
    print(f"O valor futuro é: {result}")
