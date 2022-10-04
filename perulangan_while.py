def while_dasar():
    count = 1
    while count < 10:
        # print(f'angka ke-{count}')
        print(count, end=' ')
        count += 2

def while_pangkat():
    count = 1
    while count < 10:
        print(count**2, end=' ')
        count += 1

def while_ganjil_genap():
    mode = input("masukan mode (1=Ganjil/2=Genap)= ")
    # TRAPING
    if not (mode == "1" or mode == "2"):
        print("mode tidak ditemukan")
        exit()
    # LOGIC
    start = int(input("masukan range awal = "))
    end = int(input("masukan range akhir = "))
    while start <= end:
        if mode == "1":
            if start%2 == 1: print(start, end=" ")
        elif mode == "2":
            if start%2 == 0: print(start, end=" ")
        start += 1

def while_fibonaci():
    n = int(input("Masukan n = "))
    f0, f1, f2 = 0, 1, 1
    count = 0

    while count < n:
        print(f0, end=" ")
        f2 = f0 + f1
        # update f
        f0 = f1
        f1 = f2
        count += 1

def while_fibonaci_range():
    n = int(input("Masukan batas rentang = "))
    n1, n2 = 0, 1
    while n1 < n:
        print(n1, end=' ')
        n1, n2 = n2, n1+n2


if __name__ == '__main__':
    # dipanggil ketika file ini langsunng dijalankan
    # while_pangkat()
    # while_ganjil_genap()
    while_ganjil_genap()
else:
    # dipanggil ketika file ini diimport
    print("=====PRAKTIKUM 4: Perulangan (while, for & nested loop)======")