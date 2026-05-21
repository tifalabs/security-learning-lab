import string

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add symbols.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback


password = input("Enter a password to check: ")
strength, feedback = check_password_strength(password)

print(f"\nPassword strength: {strength}")

if feedback:
    print("\nSuggestions:")
    for tip in feedback:
        print(f"- {tip}")
else:
    print("Nice. This password has strong basic structure.")