# PENJELASAN PRATIKUM 5

## NAMA : ANDI NURCAHYANA
## NIM  : 312510201

1. Mulai

Flowchart dimulai dari simbol Start (biasanya berbentuk oval).
Ini menandakan program akan dijalankan dari awal.

 2. Inisialisasi Dictionary

Langkah pertama, program membuat dictionary kosong:

mahasiswa = {}


Fungsinya untuk menyimpan semua data mahasiswa nanti.
Struktur data ini mirip seperti tabel kecil dengan format:

{
  "Yasser": {"tugas": 80, "uts": 85, "uas": 90, "akhir": 85.75}
}

 3. Tampilkan Menu Pilihan

Program menampilkan daftar menu agar pengguna bisa memilih apa yang ingin dilakukan:

1. Tambah Data
2. Ubah Data
3. Hapus Data
4. Tampilkan Data
5. Cari Data
6. Keluar

 4. Input Pilihan

Pengguna memasukkan angka 1–6 sesuai menu yang diinginkan.
Nilai input ini akan menentukan cabang (decision) selanjutnya di flowchart.

 5. Percabangan (Decision)

Flowchart berisi beberapa percabangan (kotak belah ketupat) untuk memeriksa pilihan pengguna:

Jika 1 (Tambah Data):

Program meminta input nama, nilai tugas, UTS, dan UAS.

Menghitung nilai akhir.

Menyimpan semua data ke dalam dictionary.

Setelah selesai, kembali ke menu utama.

Jika 2 (Ubah Data):

Program minta nama mahasiswa yang ingin diubah.

Jika nama ditemukan → input nilai baru → hitung ulang nilai akhir.

Jika nama tidak ada → tampilkan pesan “Data tidak ditemukan.”

Kembali ke menu utama.

Jika 3 (Hapus Data):

Program minta nama mahasiswa.

Jika nama ada → hapus dari dictionary.

Jika tidak → tampilkan pesan “Data tidak ditemukan.”

Kembali ke menu utama.

Jika 4 (Tampilkan Data):

Jika belum ada data → tampilkan pesan “Belum ada data.”

Jika sudah ada → tampilkan semua data mahasiswa dalam bentuk tabel.

Kembali ke menu utama.

Jika 5 (Cari Data):

Minta nama mahasiswa.

Jika ditemukan → tampilkan data lengkap (tugas, UTS, UAS, akhir).

Jika tidak → tampilkan “Data tidak ditemukan.”

Kembali ke menu utama.

Jika 6 (Keluar):

Program menampilkan pesan “Terima kasih!”

Lalu menuju ke langkah akhir (End).

 6. Kembali ke Menu Utama

Setelah satu proses (tambah, ubah, hapus, tampilkan, cari) selesai,
program tidak langsung berhenti, tapi kembali ke menu pilihan agar pengguna bisa melakukan hal lain tanpa menutup program.

7. Selesai (End)

Jika pengguna memilih menu 6 (Keluar), program berhenti.
Flowchart berakhir di simbol End (oval).
