from UserAuth.login_verification import register_user, login_user
from UserAuth.user_activity_logging import log_activity

def user_registration():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    register_user(username, password)
    print("User registered successfully.")

def user_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if login_user(username, password):
        log_activity(username, "Logged in successfully")
        print(f"Welcome, {username}!")
    else:
        log_activity(username, "Failed login attempt")
        print("Invalid username or password.")

def main():
    while True:
        print("\n1. Register User")
        print("2. Login User")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            user_registration()
        elif choice == '2':
            user_login()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
