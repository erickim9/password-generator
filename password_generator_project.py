import random
import string

def generate_password(length = 12, letters = True, digits = True, symbols = True):
    characters = ""
    if not (letters or digits or symbols):
        print("You must select at least one type.")

    if letters:
        characters += string.ascii_letters
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Simple Password Generator")
    try:
        length = int(input("How long do you want it to be?: "))
        letters = input("Letters in password? (y/n): ").strip().lower() == 'y'
        digits = input("Digits in password? (y/n): ").strip().lower() == 'y'
        symbols = input("Symbols in password? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, letters, digits, symbols)
        print("Generated password: " + password)

    except Exception as e:
        print("Error: " + e)

if __name__ == "__main__":
    main()
