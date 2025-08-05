import streamlit as st

if not st.session_state.get("login_status"):
    st.warning("Silakan login terlebih dahulu.")
    st.stop()

st.title("📅 Reservasi Kamar")

nama = st.text_input("Nama Lengkap", value=st.session_state["username"])
kamar = st.selectbox("Pilih Kamar", ["A1", "A2", "B1"])
durasi = st.selectbox("Durasi", ["1 Bulan", "3 Bulan", "6 Bulan"])

if st.button("Reservasi Sekarang"):
    st.success(f"Reservasi berhasil! Kamar {kamar} untuk {durasi}")
