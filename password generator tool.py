import random
import string

def generate_password(length=12, upper=True, lower=True, digits=True, symbols=True, avoid_ambiguous=True):
    """
    Generate a secure and robust password based on user-specified preferences.

    Parameters:
    - length (int): Length of the password (default is 12)
    - upper (bool): Include uppercase letters (default is True)
    - lower (bool): Include lowercase letters (default is True)
    - digits (bool): Include digits (default is True)
    - symbols (bool): Include symbols (default is True)
    - avoid_ambiguous (bool): Avoid ambiguous characters like 'I', 'l', '1', 'O', '0' (default is True)

    Returns:
    - str: Generated password
    """
    # Define character sets
    upper_chars = string.ascii_uppercase if upper else ''
    lower_chars = string.ascii_lowercase if lower else ''
    digits_chars = string.digits if digits else ''
    symbols_chars = string.punctuation if symbols else ''

    # Remove ambiguous characters
    if avoid_ambiguous:
        ambiguous_chars = 'Il10O'
        upper_chars = ''.join(char for char in upper_chars if char not in ambiguous_chars)
        lower_chars = ''.join(char for char in lower_chars if char not in ambiguous_chars)
        digits_chars = ''.join(char for char in digits_chars if char not in ambiguous_chars)
        symbols_chars = ''.join(char for char in symbols_chars if char not in ambiguous_chars)

    # Combine character sets based on user preferences
    all_chars = upper_chars + lower_chars + digits_chars + symbols_chars

    # Check if at least one character set is selected
    if not all_chars:
        raise ValueError("At least one character set (upper, lower, digits, symbols) must be selected.")

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

def main():
    print("Welcome to the Password Generation Tool!")
    try:
        # Get user preferences
        length = int(input("Enter the length of the password (default is 12): ") or 12)
        upper = input("Include uppercase letters? (y/n, default is y): ").lower() == 'y'
        lower = input("Include lowercase letters? (y/n, default is y): ").lower() == 'y'
        digits = input("Include digits? (y/n, default is y): ").lower() == 'y'
        symbols = input("Include symbols? (y/n, default is y): ").lower() == 'y'
        avoid_ambiguous = input("Avoid ambiguous characters like 'I', 'l', '1', 'O', '0'? (y/n, default is y): ").lower() == 'y'

        # Generate password
        password = generate_password(length, upper, lower, digits, symbols, avoid_ambiguous)
        
        print(f"\nGenerated Password: {password}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
