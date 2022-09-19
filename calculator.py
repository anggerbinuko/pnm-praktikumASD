# Fungsi hitung-hitungan: penjumlahan
def penjumlahan():
    angka1 = int(input("Masukkan Angka 1 : "))
    angka2 = int(input("Masukkan Angka 2 : "))
    hasil = angka1 + angka2

    print(f'Hasil dari {angka1} + {angka2} = {hasil}')

# Fungsi hitung-hitungan: pengurangan
def pengurangan():
    angka1 = int(input("Masukkan Angka 1 : "))
    angka2 = int(input("Masukkan Angka 2 : "))
    hasil = angka1 - angka2

    print(f'Hasil dari {angka1} - {angka2} = {hasil}')

# Fungsi hitung-hitungan: perkalian
def perkalian():
    angka1 = int(input("Masukkan Angka 1 : "))
    angka2 = int(input("Masukkan Angka 2 : "))
    hasil = angka1 * angka2

    print(f'Hasil dari {angka1} * {angka2} = {hasil}')

# Fungsi hitung-hitungan: perkalian
def pembagian():
    angka1 = int(input("Masukkan Angka 1 : "))
    angka2 = int(input("Masukkan Angka 2 : "))
    hasil = angka1 / angka2

    print(f'Hasil dari {angka1} / {angka2} = {hasil}')

def simple_calculator():
    print("Silahkan pilih mode:\n1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian")
    mode = int(input("Masukkan Mode : "))

    if mode == 1:
        penjumlahan()
    elif mode == 2:
        pengurangan()
    elif mode == 3:
        perkalian()
    else:
        pembagian()

simple_calculator()