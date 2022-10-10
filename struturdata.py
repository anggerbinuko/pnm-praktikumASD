# Bikin list isi ruangan lab 217 minimal 10
isi_lab216 = ["kursi", "papan tulis", "meja", "ac", "lemari",
              "komputer", "cctv", "proyektor","lampu", "kalender"]

# 1. Tampilkan seluruh item list isi_lab216
# 2. Tampilkan item indeks ke-5 dari list isi_lab216
# 3. Ubah item indeks ke-5 dari list isi_lab216
# 4. Hapus item indeks ke-5 dari list isi_lab216
# 5. Tambahkan item ke list isi_lab216 dari item indeks ke-5 yg dihapus
# 6. Tampilkan ulang seluruh item list isi_lab216

# Bikin tuple komponen hardware laptop minimal 5
hardware_laptop = ("Layar", "RAM", "CPU", "GPU", "Storage Disk")
# 1. Tampilkan seluruh item tuple hardware_laptop menggunakan iterasi/perulang for

# Bikin dictionary data KTP (NIK, TTL, Jenis Kelamin, Alamat, Agama,
# Status Perkawinan, Pekerjaan, Kewarganegaraan)
# data_ktp = {"key":"value"}
data_ktp = {"NIK":"3577020204911234",
            "TTL":"Madiun, 29 Februari 1992",
            "Jenis Kelamin":"Laki-laki",
            "Alamat":"Jl. Maleo No. 6",
            "Agama":"ISLAM",
            "Status Perkawinan":"KAWIN",
            "Pekerjaan":"Dosen",
            "Kewarganegaraan":"INDONESIA"}

# 1. Buat tampilan serupa tampilan KTP kalian
# NIK     : 357817239123
# Nama    : Angger
# dst

for i in data_ktp:
    print(f"{i} : {data_ktp[i]}")