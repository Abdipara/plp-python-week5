import random
import string

def make_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        password += random.choice(characters)  # Added line
    return password

# Generate passwords
p1 = make_password()
p2 = make_password(12)

# Print results
print("Password:", p1)
print("Length:", len(p1))
print("Password:", p2)
print("Length:", len(p2))