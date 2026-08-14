# =========================================================
# PROJECT: SISTEM PEMINJAMAN BUKU PERPUSTAKAAN SEKOLAH
# =========================================================

print("=" * 50)
print(" SISTEM PERPUSTAKAAN SEKOLAH ")
print("=" * 50)

# Input Data Siswa & Buku
nama_siswa = input("Masukkan Nama Siswa/Peminjam : ")

print("\nDaftar Buku yang Tersedia:")
print("1. Bahasa Inggris Tingkat Lanjut")
print("2. Dasar-Dasar Jaringan Komputer & Telekomunikasi")
print("3. Koding dan Kecerdasan Artifisial")
print("-" * 50)

pilihan_buku = input("Pilih Nomor Buku (1/2/3)      : ")

#  Judul Buku
if pilihan_buku == "1":
    judul_buku = "Bahasa Inggris Tingkat Lanjut"
elif pilihan_buku == "2":
    judul_buku = "Dasar-Dasar Jaringan Komputer & Telekomunikasi"
elif pilihan_buku == "3":
    judul_buku = "Koding dan Kecerdasan Artifisial"
else:
    judul_buku = "Buku Tidak Ditemukan"

# Simulasi Pengembalian & Denda
print("\n--- Status Pengembalian Buku ---")
lama_pinjam = int(input("Berapa hari buku ini dipinjam? : "))

#  contoh Aturan: Maksimal pinjam 7 hari. Lewat dari 7 hari, denda Rp1.000 per hari!
batas_pinjam = 7
if lama_pinjam > batas_pinjam:
    hari_terlambat = lama_pinjam - batas_pinjam
    denda = hari_terlambat * 1000
    status_denda = f"Terlambat {hari_terlambat} hari (Denda: Rp{denda:,})"
else:
    denda = 0
    status_denda = "Tepat Waktu (Bebas Denda)"

# Cetak Kartu Peminjaman / Resi Pengembalian
print("\n" + "=" * 50)
print("             TRANSAKSI PERPUSTAKAAN             ")
print("=" * 50)
print(f"Nama Peminjam : {nama_siswa}")
print(f"Judul Buku    : {judul_buku}")
print(f"Lama Pinjam   : {lama_pinjam} Hari")
print("-" * 50)
print(f"Status Denda  : {status_denda}")
print(f"Total Denda   : Rp{denda:,}")
print("=" * 50)
print("   Harap menjaga buku dengan baik & tidak merusaknya!   ")