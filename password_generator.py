import random
import string

print(" Strong Password Generator")

length = int(input("Enter password length (min 6): "))

if length < 6:
    print("Password too short!")
else:
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Strong Password:", password)
