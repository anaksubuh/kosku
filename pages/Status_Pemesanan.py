import streamlit as st

if not st.session_state.get("login_status"):
    st.warning("Silakan login terlebih dahulu.")
    st.stop()

st.title("📋 Status Pemesanan")
st.info("Berikut status pesanan kamu (simulasi):")

# Simulasi status
st.write("🛏️ Kamar A2 - 3 Bulan")
st.success("Status: Dikonfirmasi & Aktif")
