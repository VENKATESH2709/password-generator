import random
import string

def validate_input():
    """
    Validate and return the user input for password length.
    Ensures the input is a positive integer greater than or equal to 8.
    """
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 8): "))
            if length < 8:
                print("Password length must be at least 8 characters. Try again.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def generate_password(length):
    """
    Generate a secure random password of the specified length.
    The password will include a mix of uppercase, lowercase, numbers, and special characters.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    # Character pools
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = "@#$%&*"

    # Ensure the password contains at least one of each character type
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    """
    Main function to interact with the user and generate passwords.
    """
    print("Welcome to the Random Password Generator!")
    
    while True:
        length = validate_input()
        password = generate_password(length)
        print(f"\nYour generated password is: {password}\n")

        # Ask the user if they want to generate another password
        again = input("Would you like to generate another password? (yes/no): ").strip().lower()
        if again != 'yes':
            print("\nThank you for using the Random Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
