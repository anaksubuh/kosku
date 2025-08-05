import streamlit as st

if not st.session_state.get("login_status"):
    st.warning("Silakan login terlebih dahulu.")
    st.stop()

st.title("📊 Dashboard")
st.write(f"Selamat datang, **{st.session_state['username']}**!")

st.success("Ini adalah halaman dashboard utama.")
