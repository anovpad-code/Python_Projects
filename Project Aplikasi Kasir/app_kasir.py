# ==========================================
# PROJECT: APLIKASI KASIR DIGITAL
# ==========================================

print("=" * 40)
print("       SYSTEM KASIR STORE DIGITAL")
print("=" * 40)

# Input data transaksi
nama_pembeli = input("Masukkan Nama Pembeli : ")
nama_barang  = input("Masukkan Nama Barang  : ")
harga_satuan = int(input("Masukkan Harga Satuan (Rp) : "))
jumlah_beli  = int(input("Masukkan Jumlah Beli       : "))

# Hitung kalkulasi awal
total_awal = harga_satuan * jumlah_beli

# Sistem Diskon
diskon = 0
if total_awal >= 100000:
    diskon = 0.10 * total_awal  # Diskon 10%
    catatan_diskon = "Selamat! Anda mendapatkan diskon 10%"
else:
    catatan_diskon = "Tidak mendapat diskon (Min. belanja Rp100.000)"

total_akhir = total_awal - diskon

# Tampilan Struk Pembayaran
print("\n" + "=" * 40)
print("            STRUK PEMBAYARAN            ")
print("=" * 40)
print(f"Nama Pembeli : {nama_pembeli}")
print(f"Nama Barang  : {nama_barang}")
print(f"Jumlah Beli  : {jumlah_beli} pcs x Rp{harga_satuan:,}")
print("-" * 40)
print(f"Total Harga  : Rp{total_awal:,.0f}")
print(f"Diskon       : Rp{diskon:,.0f}")
print(f"Keterangan   : {catatan_diskon}")
print("-" * 40)
print(f"TOTAL BAYAR  : Rp{total_akhir:,.0f}")
print("=" * 40)
print("  Terima Kasih Telah Berbelanja Bersama Kami!  ")