from generator import PasswordGenerator

def menu():
    print("\n===================================")
    print("  Bem-vindo ao Gerador de Senhas!")
    print("===================================\n")

    length = int(input("Digite o comprimento da senha: "))
    use_uppercase = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    use_lowercase = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    use_digits = input("Incluir números? (s/n): ").lower() == 's'
    use_special = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

    generator = PasswordGenerator(
        length=length,
        use_uppercase=use_uppercase,
        use_lowercase=use_lowercase,
        use_digits=use_digits,
        use_special=use_special
    )

    password = generator.generate()
    print(f"\nSua nova senha é: {password}")