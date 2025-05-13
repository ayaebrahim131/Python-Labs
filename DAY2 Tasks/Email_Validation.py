def verify_user():
    user_data = {}
    
    # Name validation section
    def get_valid_name():
        while 1:
            user_input = input("What is your name? ").strip()
            if not user_input:
                print("Sorry, the name field cannot be empty")
                continue
            if user_input.isdigit():
                print("Please enter a real name, not just numbers")
                continue
            return user_input
    
    # Email validation section
    def get_valid_email():
        while 1:
            email_input = input("What is your email address? ").strip()
            parts = email_input.split('@')
            if len(parts) != 2 or not parts[0] or '.' not in parts[1]:
                print("Email must contain @ and a dot after it")
                continue
            return email_input
    
    user_data['Name'] = get_valid_name()
    user_data['Email'] = get_valid_email()
    
    print("\nData registered successfully!")
    print("="*30)
    for key, value in user_data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    verify_user()