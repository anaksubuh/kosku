import sqlite3
import hashlib

# Koneksi database
def get_connection():
    return sqlite3.connect("data_user.db", check_same_thread=False)

# Hash password sebelum disimpan atau dicek
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Buat tabel user jika belum ada
def create_user_table():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Tambah user baru
def add_user(username, password):
    conn = get_connection()
    c = conn.cursor()
    hashed = hash_password(password)
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
    conn.commit()
    conn.close()

# Cek apakah username sudah dipakai
def user_exists(username):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    data = c.fetchone()
    conn.close()
    return data is not None

# Validasi login: username dan password (dengan hash)
def validate_login(username, password):
    conn = get_connection()
    c = conn.cursor()
    hashed = hash_password(password)
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed))
    data = c.fetchone()
    conn.close()
    return data is not None
