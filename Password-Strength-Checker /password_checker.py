# Password Strength Checker
# Created by Maurine Kyalo

import re

def check_password_strength(password):
    score = 0
    
    # 1. Check Length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
        
    # 2. Check for Lowercase and Uppercase
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
        
    # 3. Check for Numbers
    if re.search(r"\d", password):
        score += 1
        
    # 4. Check for Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        
    # Determine strength based on score
    if score >= 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak(Needs improvement)"

# Run the tool
if __name__ == "__main__":
    print("--- Password Strength Checker ---")
    user_password = input("Enter a password to test: ")
    result = check_password_strength(user_password)
    print(f"Password Strength: {result}")