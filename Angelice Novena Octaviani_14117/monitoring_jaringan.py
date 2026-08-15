import os
import time
from datetime import datetime

# --- BAGIAN 1: FUNGSI NETWORKING (CEK KONEKSI) ---
def cek_ping(host):
    """
    Melakukan ping ke host. 
    Menggunakan '-n 1' untuk Windows. 
    Jika saya menggunakan Linux/WSL, maka akan saya ganti '-n' menjadi '-c'.
    """
    # '> nul' digunakan agar output asli ping tidak mengotori terminal
    respons = os.system(f"ping -n 1 {host} > nul") 
    if respons == 0:
        return "Aktif"
    else:
        return "Tidak Aktif"

# --- BAGIAN 2: LOGIKA AI SEDERHANA (RULE-BASED CLASSIFICATION) ---
def klasifikasi_status_ai(log_results):
    """
    Menganalisis daftar status untuk memberikan kesimpulan otomatis.
    Ini memenuhi elemen AI/Rule-based pada kisi-kisi ASAS.
    """
    total_host = len(log_results)
    mati = sum(1 for status in log_results if status == "Tidak Aktif")

    if mati == 0:
        return "AMAN: Jaringan stabil dan semua host merespons."
    elif mati == total_host:
        return "BAHAYA: Koneksi terputus total! Periksa kabel atau modem."
    else:
        return f"PERINGATAN: Terdeteksi gangguan pada {mati} host. Potensi masalah jaringan!"

# --- BAGIAN 3: PROGRAM UTAMA (ALGORITMA) ---
def main():
    # Daftar host yang akan dimonitor (bisa saya tambah/ubah)
    hosts = ["8.8.8.8", "google.com", "192.168.1.1"] 
    status_sekarang = []
    log_untuk_file = []

    print("="*45)
    print("SISTEM MONITORING JARINGAN BERBASIS AI")
    print(f"Waktu Mulai: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*45)

    for h in hosts:
        hasil = cek_ping(h)
        status_sekarang.append(hasil)
        
        waktu = datetime.now().strftime("%H:%M:%S")
        info = f"[{waktu}] Host: {h:15} | Status: {hasil}"
        print(info)
        log_untuk_file.append(info)
        
        time.sleep(1) # Jeda agar tidak membebani prosesor

    # Analisis menggunakan AI Sederhana
    kesimpulan = klasifikasi_status_ai(status_sekarang)
    
    print("-"*45)
    print(f"KESIMPULAN AI: {kesimpulan}")
    print("="*45)

    # --- BAGIAN 4: SIMPAN KE FILE (LOG) ---
    # File ini akan otomatis dibuat di folder yang sama dengan skrip
    try:
        with open("log_jaringan.txt", "a") as f:
            f.write(f"\n--- Sesi Monitoring: {datetime.now()} ---\n")
            f.write("\n".join(log_untuk_file) + "\n")
            f.write(f"Hasil Analisis AI: {kesimpulan}\n")
        print("[Sistem] Berhasil menyimpan log ke 'log_jaringan.txt'")
    except Exception as e:
        print(f"[Error] Gagal menyimpan file: {e}")

if __name__ == "__main__":
    main()
