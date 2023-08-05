import random
import string
import sys
import pyperclip

class PasswordGenerator:
    def __init__(
        self,
        length=12,
        include_uppercase=True,
        include_lowercase=True,
        include_numbers=True,
        include_special_characters=True,
    ):
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_lowercase = include_lowercase
        self.include_numbers = include_numbers
        self.include_special_characters = include_special_characters

    def generate_character_pool(self):
        character_pool = []
        if self.include_uppercase:
            character_pool += list(string.ascii_uppercase)
        if self.include_lowercase:
            character_pool += list(string.ascii_lowercase)
        if self.include_numbers:
            character_pool += list(string.digits)
        if self.include_special_characters:
            character_pool += list("!@#$%^&*();:'.?")
        return character_pool

    def generate_password(self):
        character_pool = self.generate_character_pool()
        password = ''.join(random.choice(character_pool) for _ in range(self.length))
        return password

def main():
    if len(sys.argv) > 1:
        custom_length = int(sys.argv[1])
        passwordGenerator = PasswordGenerator(length=custom_length)
    else:
        passwordGenerator = PasswordGenerator()

    password = passwordGenerator.generate_password()
    pyperclip.copy(password)
    print(f"Your new password: - {password} - was copied to your clipboard!")

if __name__ == "__main__":
    main()
