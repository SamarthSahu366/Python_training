import hashlib

class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password_hash = self.__hash_password(password)

    def __hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def set_password(self, old_password, new_password):
        if self.__verify_password(old_password):
            self.__password_hash = self.__hash_password(new_password)
            print("password updated successfully.")
        else:
            print("incorrect old password. password not changed.")

    def __verify_password(self, password):
        return self.__password_hash == self.__hash_password(password)

    def check_password(self, password):
        if self.__verify_password(password):
            print("password verified successfully.")
        else:
            print("incorrect password.")

if __name__ == "__main__":
    username = input("enter your username: ")
    password = input("enter your password: ")
    account = UserAccount(username, password)

    entered_password = input("enter password to check: ")
    account.check_password(entered_password)

    old_password = input("enter old password to update: ")
    new_password = input("enter new password: ")
    account.set_password(old_password, new_password)
    entered_password = input("enter new password to check: ")
    account.check_password(entered_password)
