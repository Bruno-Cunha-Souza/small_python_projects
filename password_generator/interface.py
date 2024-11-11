from generator import PasswordGenerator

def menu():
    print("\n===================================")
    print("  Welcome to Password Generator!")
    print("===================================\n")

    length = int(input("Enter password length: "))
    use_uppercase = input("Include capital letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    generator = PasswordGenerator(
        length=length,
        use_uppercase=use_uppercase,
        use_lowercase=use_lowercase,
        use_digits=use_digits,
        use_special=use_special
    )

    password = generator.generate()
    print(f"\nYour new password is: {password}")