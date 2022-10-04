count, jmlnRataMhs = 0, 0
jmlMhs = int(input("Masukan jml Mhs = "))
# Proses perulangan hingga mhs ke-n
while count < jmlMhs:
    n = count+1
    # Input Nilai UTS & UAS
    nUTS = int(input(f"Masukan nilai UTS Mhs ke-{n} = "))
    nUAS = int(input(f"Masukan nilai UAS Mhs ke-{n} = "))
    # Proses Hitung Nilai Rata2 Mhs
    nRataMhs = (nUTS+nUAS)/2
    # Kondisional Keterangan Lulus/Tidak lulus
    if nRataMhs < 60:
        print(f"Nilai rata2 mahasiswa ke-{n} = {nRataMhs}, dinyatakan TIDAK LULUS")
    else:
        print(f"Nilai rata2 mahasiswa ke-{n} = {nRataMhs}, dinyatakan LULUS")
    # Menghitung total nilai rata2 mahasiswa
    jmlnRataMhs += nRataMhs
    # Counter +1
    count += 1
# Proses hitung nilai Rata2 Kelas
nRataKelas = jmlnRataMhs/jmlMhs
print("=========================================")
# Kondisional keterangan predikat kelas
if nRataKelas >= 70:
    print("Nilai Rata2 Kelas mendapat Predikat A")
elif 50 < nRataKelas < 70:
    print("Nilai Rata2 Kelas mendapat Predikat B")
else:
    print("Nilai Rata2 Kelas mendapat Predikat C")
