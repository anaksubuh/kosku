import streamlit as st
import os

# Cek login
if not st.session_state.get("login_status"):
    st.warning("Silakan login terlebih dahulu.")
    st.stop()

st.title("🏡 Lihat Kamar")
st.info("Berikut adalah daftar kamar kos yang tersedia:")

# Data kamar
kamar_list = [
    {
        "nomor": "A1",
        "tipe": "Standard",
        "harga": "Rp 500.000",
        "luas": "3x3 m",
        "fasilitas": ["Kamar Mandi Dalam", "AC", "Kasur", "Meja", "Lemari"],
        "gambar": "image/kamar_kos_1.jpg"
    },
    {
        "nomor": "A2",
        "tipe": "Deluxe",
        "harga": "Rp 700.000",
        "luas": "4x3 m",
        "fasilitas": ["Kamar Mandi Dalam", "AC", "Kasur", "Meja", "Lemari", "Jendela"],
        "gambar": "image/kamar_kos_2.jpg"
    },
    {
        "nomor": "B1",
        "tipe": "Premium",
        "harga": "Rp 1.000.000",
        "luas": "5x4 m",
        "fasilitas": ["Kamar Mandi Dalam", "AC", "Kasur King", "Meja", "Lemari Besar", "TV", "WiFi"],
        "gambar": "image/kamar_kos_3.jpg"
    }
]

# Loop kamar
for kamar in kamar_list:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if os.path.exists(kamar["gambar"]):
            st.image(kamar["gambar"], width=250, caption=f"Kamar {kamar['nomor']}")
        else:
            st.error(f"Gambar tidak ditemukan: {kamar['gambar']}")

    with col2:
        st.subheader(f"Kamar {kamar['nomor']} - {kamar['tipe']}")
        st.markdown(f"**Harga:** {kamar['harga']}")
        st.markdown(f"**Luas:** {kamar['luas']}")
        st.markdown("**Fasilitas:**")
        for f in kamar["fasilitas"]:
            st.markdown(f"- {f}")
        st.button(f"Pesan Kamar {kamar['nomor']}")

    st.markdown("---")
