count = 0
jmlnRataMhs = 0
jmlMhs = int(input("jumlah mahasiswa = "))

# Proses pengulangan input nilai UTS & UAS tiap mahasiswa
for i in range(0, jmlMhs):
    n = i + 1
    nUTS = int(input(f"masukan nilai UTS mahasiswa ke-{n} = "))
    nUAS = int(input(f"masukan nilai UAS mahasiswa ke-{n} = "))
    # Proses hitung nilai rata2 mahasiswa ke-n
    nRataMhs = (nUTS+nUAS)/2

    # Proses pengecekan kondisi kelulusan mahasiswa ke-n
    if nRataMhs >= 60:
        print(f"Mahasiswa ke-{n}: Anda LULUS")
    else:
        print(f"Mahasiswa ke-{n}: Anda TIDAK LULUS")

    # Proses hitung Jumlah Nilai Rata2 Mahasiswa
    jmlnRataMhs += nRataMhs
    # # Proses hitung nilai rata2 Kelas
    # nRataKelas = nRataMhs/jmlMhs

# Proses hitung nilai rata2 Kelas
nRataKelas = jmlnRataMhs/jmlMhs

# Proses pengecekann kondisi predikat kelas
print("=======================================")
if nRataKelas >= 70:
    print(f"Nilai rata2 Kelas: {nRataKelas}\nPredikat Kelas: A")
elif nRataKelas >= 50:
    print(f"Nilai rata2 Kelas: {nRataKelas}\nPredikat Kelas: B")
else:
    print(f"Nilai rata2 Kelas: {nRataKelas}\nPredikat Kelas: C")