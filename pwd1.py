"""Simple Password Strength Checker with retry loop."""

levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]

while True:
    password = input("Enter your password: ")

    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in "!@#$%^&*()_+" for c in password):
        strength += 1

    # Cap index to avoid going out of range
    idx = strength if strength < len(levels) else len(levels) - 1
    print(f"Password strength: {levels[idx]}")

    again = input("Try another? (y/n): ").strip().lower()
    if again != "y":
        print("Goodbye!")
        break
