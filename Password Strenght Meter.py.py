#import re

def check_password_strength(password):
    strength = 0
    remarks = "Weak"
    
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    
    if strength >= 4:
        remarks = "Strong"
    elif strength == 3:
        remarks = "Moderate"
    
    return strength, remarks

password = input("Enter a password: ")
strength, remarks = check_password_strength(password)
print(f"Password Strength: {strength}/5 ({remarks})")
