import re


def assess_password_strength(password):
    # Initialize score
    score = 0
    feedback = []

    # Check password length (minimum length of 8 characters is good practice)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters (non-alphanumeric)
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Give feedback on the strength of the password based on score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Return results
    return strength, feedback


# Example usage
password = input("Enter your password to assess its strength: ")
strength, feedback = assess_password_strength(password)

print(f"Password Strength: {strength}")
for line in feedback:
    print(line)
