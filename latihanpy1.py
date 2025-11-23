# Program Daftar Nilai Mahasiswa

mahasiswa = {}

def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

while True:
    print("\n=== MENU PILIHAN ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == '1':
        print("\n--- Tambah Data ---")
        nama = input("Nama Mahasiswa: ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        akhir = hitung_nilai_akhir(tugas, uts, uas)
        mahasiswa[nama] = {'tugas': tugas, 'uts': uts, 'uas': uas, 'akhir': akhir}
        print(f"Data {nama} berhasil ditambahkan!")

    elif pilihan == '2':
        print("\n--- Ubah Data ---")
        nama = input("Masukkan nama mahasiswa yang akan diubah: ")
        if nama in mahasiswa:
            tugas = float(input("Nilai Tugas baru: "))
            uts = float(input("Nilai UTS baru: "))
            uas = float(input("Nilai UAS baru: "))
            akhir = hitung_nilai_akhir(tugas, uts, uas)
            mahasiswa[nama] = {'tugas': tugas, 'uts': uts, 'uas': uas, 'akhir': akhir}
            print(f"Data {nama} berhasil diubah!")
        else:
            print("Nama tidak ditemukan!")

    elif pilihan == '3':
        print("\n--- Hapus Data ---")
        nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
        if nama in mahasiswa:
            del mahasiswa[nama]
            print(f"Data {nama} berhasil dihapus!")
        else:
            print("Nama tidak ditemukan!")

    elif pilihan == '4':
        print("\n--- Daftar Nilai Mahasiswa ---")
        if mahasiswa:
            print("{:<20} {:<10} {:<10} {:<10} {:<10}".format("Nama", "Tugas", "UTS", "UAS", "Akhir"))
            print("-" * 60)
            for nama, nilai in mahasiswa.items():
                print("{:<20} {:<10} {:<10} {:<10} {:<10.2f}".format(
                    nama, nilai['tugas'], nilai['uts'], nilai['uas'], nilai['akhir']))
        else:
            print("Belum ada data mahasiswa.")

    elif pilihan == '5':
        print("\n--- Cari Data ---")
        nama = input("Masukkan nama mahasiswa yang dicari: ")
        if nama in mahasiswa:
            nilai = mahasiswa[nama]
            print(f"Nama: {nama}")
            print(f"Nilai Tugas: {nilai['tugas']}")
            print(f"Nilai UTS: {nilai['uts']}")
            print(f"Nilai UAS: {nilai['uas']}")
            print(f"Nilai Akhir: {nilai['akhir']:.2f}")
        else:
            print("Data tidak ditemukan!")

    elif pilihan == '6':
        print("Keluar dari program. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
