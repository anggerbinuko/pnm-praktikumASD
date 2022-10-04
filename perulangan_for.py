def for_dasar():
    for i in range(1,10,+2):
        print(i, end=' ')

def for_pangkat():
    for i in range(1,10):
        print(i**2, end=' ')

def for_ganjil_genap():
    mode = input("masukan mode (1=Ganjil/2=Genap)= ")
    # TRAPING
    if not (mode == "1" or mode == "2"):
        print("mode tidak ditemukan")
        exit()
    # LOGIC
    start = int(input("masukan range awal = "))
    end = int(input("masukan range akhir = "))
    for i in range(start,end):
        if mode == "1":
            if i%2 == 1: print(i, end=" ")
        elif mode == "2":
            if i%2 == 0: print(i, end=" ")

# Pemanggilan fungsi
if __name__ == '__main__':
    # dipanggil ketika file ini langsunng dijalankan
    for_ganjil_genap()
else:
    # dipanggil ketika file ini diimport
    print("=====PRAKTIKUM 5: Perulangan (while, for & nested loop)======")