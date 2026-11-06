"""Program to check the validity of a password."""

def check_the_validity_of_a_password():
    """Validate a password based on specific criteria."""
    passwords = [
        "Password123!",
        "weak",
        "NoSpecialChar1",
        "Short1!",
        "ValidPass123!",
    ]
    special_chars = set('!@#$%^&*(),.?":{}|<>')

    for pwd in passwords:
        has_lower = any(ch.islower() for ch in pwd)
        has_upper = any(ch.isupper() for ch in pwd)
        has_digit = any(ch.isdigit() for ch in pwd)
        has_special = any(ch in special_chars for ch in pwd)
        is_valid = len(pwd) >= 8 and has_lower and has_upper and has_digit and has_special

        if is_valid:
            print(f'"{pwd}" is a VALID password.')
        else:
            print(f'"{pwd}" is an INVALID password.')

if __name__ == "__main__":
    check_the_validity_of_a_password()
