import streamlit as st

if not st.session_state.get("login_status"):
    st.warning("Silakan login terlebih dahulu.")
    st.stop()

if st.session_state.get("role") != "admin":
    st.error("⛔ Hanya admin yang bisa mengakses halaman ini.")
    st.stop()

st.title("🛠️ Manajemen Kamar")
st.success("Selamat datang Admin!")

st.write("📦 Di sini kamu bisa menambah, menghapus, atau mengedit data kamar kos.")
