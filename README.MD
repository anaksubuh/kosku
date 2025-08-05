✅ MODUL / MENU WAJIB (CORE FEATURES)
1. Dashboard Utama

    Menampilkan ringkasan data (jumlah kamar kosong, kamar terisi, jumlah user aktif).

    Bisa beda tampilan untuk admin dan user (mahasiswa).

2. Data Kamar

    List semua kamar kos beserta:

        Nomor kamar

        Harga per bulan

        Status (Kosong / Terisi / Dibooking)

        Fasilitas kamar (AC, KM dalam, wifi, dll)

        Foto kamar

    Fitur pencarian dan filter (misal: harga < 1jt, ada AC).

3. Pemesanan / Reservasi Kamar

    Form pemesanan: pilih kamar, lama sewa, tanggal masuk.

    Simpan ke database.

    Tampilkan status: “Menunggu Konfirmasi” / “Berhasil” / “Gagal”.

4. Konfirmasi & Riwayat Reservasi

    Untuk mahasiswa: lihat status pesanan mereka.

    Untuk admin: tampilkan list pemesanan masuk, konfirmasi/terima/tolak.

⚙️ MODUL PENDUKUNG (ADMIN)
5. Manajemen Kamar

    Tambah/Edit/Hapus data kamar

    Upload foto kamar

    Set harga dan status kamar

6. Manajemen User

    List semua user

    Blokir user jika perlu

    Reset password

7. Laporan dan Statistik

    Berapa kamar terisi setiap bulan

    Grafik pendapatan dari kos

    Laporan pemesanan

💬 FITUR TAMBAHAN (OPSIONAL TAPI BERGUNA)
8. Notifikasi

    Notif jika ada pesanan baru (untuk admin)

    Notif kalau pemesanan dikonfirmasi (untuk user)

9. Sistem Pembayaran

    Bisa integrasi pembayaran (simulasi / real seperti Midtrans, Xendit, dll)

    Upload bukti transfer

10. Live Chat / Kontak Admin

    Form atau chat mini untuk bertanya

11. Rating & Ulasan

    Mahasiswa bisa memberi rating dan review kamar

🧱 STRUKTUR HALAMAN UMUM DI STREAMLIT

    home() → landing page

    login_page() / register_page()

    dashboard_user() dan dashboard_admin()

    room_list()

    booking_form()

    reservation_status()

    admin_manage_rooms()

    admin_manage_users()

    report_page()