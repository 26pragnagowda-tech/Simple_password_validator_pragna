import string

password = input("Enter your password: ")

errors = []

if len(password) < 8:
    errors.append("At least 8 characters are required.")

if not any(c.isupper() for c in password):
    errors.append("Include at least one uppercase letter.")

if not any(c.islower() for c in password):
    errors.append("Include at least one lowercase letter.")

if not any(c.isdigit() for c in password):
    errors.append("Include at least one number.")

if not any(c in string.punctuation for c in password):
    errors.append("Include at least one special character.")

if errors:
    print("Invalid password!")
    for error in errors:
        print("-", error)
else:
    print("Password is valid!")
