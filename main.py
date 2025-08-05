import streamlit as st

# Konfigurasi tampilan halaman
st.set_page_config(
    page_title="Aplikasi Kos",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Fungsi untuk auto-tutup sidebar
def auto_close_sidebar():
    hide_sidebar = """
        <script>
        const sidebar = parent.document.querySelector('section[data-testid="stSidebar"]');
        const toggle = parent.document.querySelector('button[title="Toggle sidebar"]');
        if (sidebar && toggle) {
            toggle.click();
        }
        </script>
    """
    st.markdown(hide_sidebar, unsafe_allow_html=True)

# Judul & deskripsi
st.title("🏠 Aplikasi Reservasi Kos Mahasiswa")
st.info("Silakan pilih halaman di sidebar: **Login** atau **Registrasi** untuk melanjutkan.")

# Tombol menuju dashboard (simulasi)
if st.button("Masuk ke Dashboard"):
    # Misalnya kamu arahkan pakai session_state
    st.session_state["login_status"] = True
    st.session_state["username"] = "guest"
    
    # Tutup sidebar otomatis (khusus HP)
    auto_close_sidebar()
    
    st.success("Berhasil masuk sebagai guest.")
    st.balloons()
