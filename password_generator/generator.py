import random
import string

class PasswordGenerator:
    def __init__(self, length=8, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_lowercase = use_lowercase
        self.use_digits = use_digits
        self.use_special = use_special

    def generate(self):
        characters = ''
        if self.use_uppercase:
            characters += string.ascii_uppercase
        if self.use_lowercase:
            characters += string.ascii_lowercase
        if self.use_digits:
            characters += string.digits
        if self.use_special:
            characters += string.punctuation

        if not characters:
            raise ValueError("No character types selected for password generation")

        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password
