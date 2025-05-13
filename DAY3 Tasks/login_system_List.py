def check_user(users_list, username, password):
    
    for user in users_list:
        if username == user["name"]:
            if password == user["pass"]:
                return True
            else:
                print("Wrong password")
                return False
    return None

def login_system():
    
    users = [
        {"name": "aya", "pass": "123"},
        {"name": "ebrahim", "pass": "456"}
    ]
    
    while True:
        entered_name = input("Enter your name: ")
        
        user_found = False
        for user in users:
            if entered_name == user["name"]:
                user_found = True

                while True:
                    password = input("Enter your password: ")
                    if check_user(users, entered_name, password):
                        print("Authorized user, Welcome")
                        return  
        
        if not user_found:
            print("Access Denied")
            

login_system()