import streamlit as st

if st.session_state.get("role") != "admin":
    st.warning("Hanya admin yang bisa melihat laporan.")
    st.stop()

st.title("Laporan Pemesanan")

st.write("Total pemasukan bulan ini: Rp2.500.000")
st.write("Total kamar terisi: 7 dari 10")
