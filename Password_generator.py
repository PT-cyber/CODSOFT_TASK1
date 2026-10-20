import string
import secrets

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Generates a random password based on user preferences."""
    characters = ""
    
    # Build the pool of allowed characters
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Fallback in case the user says 'no' to everything
    if not characters:
        return None

    # Generate the password using the 'secrets' module for better security
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("=" * 40)
    print("🔒 WELCOME TO THE SECURE PASSWORD GENERATOR 🔒")
    print("=" * 40)

    while True:
        # 1. Get Password Length
        try:
            length = int(input("\nEnter desired password length (e.g., 8, 12, 16): "))
            if length < 4:
                print("⚠️ For security reasons, length should be at least 4. Please try again.")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")
            continue

        # 2. Get Complexity Preferences
        print("\nSelect character types to include (y/n):")
        use_upper = input("Include Uppercase letters (A-Z)? ").strip().lower() == 'y'
        use_lower = input("Include Lowercase letters (a-z)? ").strip().lower() == 'y'
        use_digits = input("Include Numbers (0-9)? ").strip().lower() == 'y'
        use_symbols = input("Include Symbols (!@#$%^&*)? ").strip().lower() == 'y'

        # 3. Generate and Display Password
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

        if password:
            print("\n" + "*" * 40)
            print(f"✨ Your Generated Password: {password}")
            print("*" * 40 + "\n")
        else:
            print("\n❌ Error: You must select at least one character type to generate a password.\n")
            continue

        # 4. Ask to play again
        play_again = input("Do you want to generate another password? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\n👋 Exiting Password Generator. Stay secure!")
            break

if __name__ == "__main__":
    main()
