from mail_verification import validate_input

def main():
    print("=== Email and Username Validation ===")
    username, email = validate_input() 
    print("\nFinal Output:")
    print(f"Username: {username}")
    print(f"Email: {email}")

if __name__ == "__main__":
    main()