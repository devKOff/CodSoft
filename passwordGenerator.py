import string
import random

# creating a function which has password generator function
# 1 taking no. of character in password
# generate a password from random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the Number of characters you wish to generate: "))
        if length < 4:
            print("Password length should be at least 4 characters.")
            return

        password = generate_password(length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
