import random
import string

def generate_password(length):
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    remaining = ''.join(
        random.choice(
            string.ascii_letters + string.digits + string.punctuation
        ) for _ in range(length - 4)
    )

    password_list = list(lowercase + uppercase + digit + special + remaining)
    random.shuffle(password_list)

    return ''.join(password_list)

try:
    length = int(input("Enter password length (minimum 4): "))

    if length < 4:
        print("Password length must be at least 4.")
    else:
        print("\nGenerated Password:", generate_password(length))

except ValueError:
    print("Please enter a valid number.")
