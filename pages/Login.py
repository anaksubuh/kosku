import streamlit as st
from auth_session import validate_login, get_user_role, save_session, load_session, clear_session

# Cek apakah ada sesi login
session = load_session()
st.session_state.update(session)

if st.session_state.get("login_status", False):
    st.success(f"Sudah login sebagai {st.session_state['username']} ({st.session_state['role']})")
    if st.button("Logout"):
        clear_session()
        st.session_state.clear()
        st.success("Berhasil logout.")
        st.rerun()
    st.stop()

# Form login
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if validate_login(username, password):
        role = get_user_role(username)
        st.session_state.update({"login_status": True, "username": username, "role": role})
        save_session(username, role)
        st.success(f"Login berhasil sebagai {username}")
        st.rerun()
    else:
        st.error("Username atau password salah.")
