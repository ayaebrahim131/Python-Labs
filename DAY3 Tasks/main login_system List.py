from login_system_List import login_system

def main():
    print("=== Login System ===")
    username = login_system()  
    if username:
        print(f"\nLogin successful for user: {username}")
    else:
        print("\nLogin failed")

if __name__ == "__main__":
    main()