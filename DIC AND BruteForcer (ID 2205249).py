import itertools
import string
import time

# Load password dictionary from a file
def load_dictionary(filename):
    """Load passwords from a dictionary file into a set for faster lookup."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return set(line.strip() for line in file.readlines())
    except FileNotFoundError:
        print("Error: Dictionary file not found!")
        return set()

# Perform Dictionary Attack
def dictionary_attack(username, target_password, dictionary):
    """Try passwords from the dictionary to match the target password."""
    print(f"\nAttempting Dictionary Attack for user: {username}...")
    start_time = time.time()

    if target_password in dictionary:
        elapsed_time = time.time() - start_time
        print(f"Success! Password for {username} found: {target_password} in {elapsed_time:.2f} seconds.")
        return True

    elapsed_time = time.time() - start_time
    print(f"Dictionary attack failed after {elapsed_time:.2f} seconds.")
    return False

# Perform Brute Force Attack
def brute_force_attack(username, target_password, show_attempts=False):
    """Try every possible 5-letter combination until the password is found."""
    print(f"\nStarting Brute Force Attack for user: {username}...")
    start_time = time.time()
    attempts = 0
    characters = string.ascii_letters  # A-Z, a-z

    for attempt in itertools.product(characters, repeat=5):
        attempts += 1
        guess = ''.join(attempt)

        if show_attempts:
            print(f"Trying: {guess} | Attempt: {attempts}")

        if guess == target_password:
            elapsed_time = time.time() - start_time
            print(f"\nSuccess! Password for {username} found: {guess} in {elapsed_time:.2f} seconds after {attempts} attempts.")
            return True

    elapsed_time = time.time() - start_time
    print(f"Brute force attack failed after {elapsed_time:.2f} seconds and {attempts} attempts.")
    return False

# Validate password input
def validate_password(password):
    """Ensure the password is exactly 5 letters long and contains only alphabets."""
    if len(password) != 5:
        print("\nError: Password must be exactly 5 letters long!")
        return False
    if not password.isalpha():
        print("\nError: Password must contain only alphabetic characters (A-Z, a-z)!")
        return False
    return True

# Main function
def main():
    print("\n🔹 mohamed ahmed aly mobarak anu 🔹\n")
    
    # Get user input
    username = input("Enter username: ").strip()
    while not username:
        print("Error: Username cannot be empty!")
        username = input("Enter username: ").strip()
    
    while True:
        target_password = input(f"Enter the password to crack for {username} (5 letters only): ").strip()
        if validate_password(target_password):
            break
    
    # Load password dictionary
    dictionary = load_dictionary("dictionary.txt")

    # Try dictionary attack first
    if not dictionary_attack(username, target_password, dictionary):
        # If dictionary attack fails, perform brute force attack
        show_attempts = input("\nDo you want to see all attempts? (y/N): ").strip().lower() == 'y'
        brute_force_attack(username, target_password, show_attempts)

if __name__ == "__main__":
    main()
