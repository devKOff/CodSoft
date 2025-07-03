import string
import random

def generate_password(length):
    # Define characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose 'length' characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password length should be at least 4 characters.")
            return

        password = generate_password(length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
