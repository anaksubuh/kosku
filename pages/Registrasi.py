import streamlit as st
from auth_session import add_user, user_exists

st.title("📝 Registrasi")

username = st.text_input("Username")
password = st.text_input("Password", type="password")
confirm = st.text_input("Konfirmasi Password", type="password")

if st.button("Daftar"):
    if not username or not password or not confirm:
        st.warning("Harap isi semua kolom.")
    elif password != confirm:
        st.error("Password tidak cocok.")
    elif user_exists(username):
        st.error("Username sudah digunakan.")
    else:
        add_user(username, password)
        st.success("Registrasi berhasil! Silakan login.")
