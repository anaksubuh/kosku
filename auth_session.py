import json
import hashlib
import os


SESSION_FILE = "session.json"

def save_session(username, role):
    with open(SESSION_FILE, "w") as f:
        json.dump({"username": username, "role": role, "login_status": True}, f)

def load_session():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as f:
            return json.load(f)
    return {"login_status": False}

def clear_session():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)

DB_PATH = "users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists(DB_PATH):
        return {}
    with open(DB_PATH, "r") as file:
        return json.load(file)

def save_users(users):
    with open(DB_PATH, "w") as file:
        json.dump(users, file, indent=4)

def add_user(username, password, role="user"):
    users = load_users()
    users[username] = {
        "password": hash_password(password),
        "role": role
    }
    save_users(users)

def user_exists(username):
    users = load_users()
    return username in users

def validate_login(username, password):
    users = load_users()
    if username in users:
        return users[username]["password"] == hash_password(password)
    return False

def get_user_role(username):
    users = load_users()
    return users.get(username, {}).get("role", "user")
