import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def get_valid_password_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Invalid length! Please Enter a positive length for the password.")
            else:
                return length
        except ValueError:
            print("Invalid length! Please enter a valid length (a positive integer).")
def main():
    length = get_valid_password_length()
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
