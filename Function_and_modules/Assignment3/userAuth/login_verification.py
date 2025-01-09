from UserAuth.password_hashing import hash_password, verify_password

users_db = {}

def register_user(username, password):
    hashed_password = hash_password(password)
    users_db[username] = hashed_password

def login_user(username, password):
    if username in users_db:
        if verify_password(users_db[username], password):
            return True
    return False
