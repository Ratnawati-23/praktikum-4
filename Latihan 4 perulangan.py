# Program memasukkan data sebanyak-banyaknya
data_mahasiswa = []

while True:
    print("\nMasukkan Data Mahasiswa")
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    # Hitung nilai akhir
    nilai_akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)

    # Simpan ke list
    data_mahasiswa.append({
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir
    })

    # Pertanyaan lanjut
    lanjut = input("Tambah data lagi? (y/t): ").lower()
    if lanjut == "t":
        break

# Tampilkan hasil
print("\n=== DAFTAR DATA MAHASISWA ===")
for m in data_mahasiswa:
    print(f"Nama: {m['nama']}")
    print(f"Nilai Tugas: {m['tugas']}")
    print(f"Nilai UTS: {m['uts']}")
    print(f"Nilai UAS: {m['uas']}")
    print(f"Nilai Akhir: {m['nilai_akhir']:.2f}")
    print("------------------------------")
