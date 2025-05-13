def validate_input():
    while True:
        errors = []  

        username = input("Enter a username: ").strip()
        email = input("Enter your email: ").strip()

        if not username:
            errors.append("Username cannot be empty.")
        else:
            username = username.replace("_", "").replace("-", "")
            if not any(char.isalpha() for char in username):
                errors.append("Username must contain at least one letter (a-z, A-Z).")
            elif not username.isalnum():
                errors.append("Username can only contain letters (a-z, A-Z), numbers (0-9), underscores (_), or hyphens (-).")

        if '@' not in email or '.' not in email:
            errors.append("Invalid email: '@' and '.' must exist.")
        else:
            at_index = email.find('@')
            dot_index = email.find('.', at_index)

            if at_index <= 0:
                errors.append("Invalid email: '@' cannot be at the beginning or missing.")
            if dot_index == -1:
                errors.append("Invalid email: '.' must appear after '@'.")
            elif dot_index - at_index <= 1:
                errors.append("Invalid email: There must be at least one character between '@' and '.'.")
            if email.endswith('@') or email.endswith('.'):
                errors.append("Invalid email: Email cannot end with '@' or '.'.")

        if errors:
            print("\nValidation errors:")
            for error in errors:
                print("=>", error)
            print()
        else:
            print("\nCongratulations! Your username and Email are valid!")
            return username, email 

if __name__ == "__main__":
    validate_input()