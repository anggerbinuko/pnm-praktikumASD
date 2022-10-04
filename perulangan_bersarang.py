def bariskolom_while():
    baris = 1
    while baris < 4:
        kolom = 1
        while kolom < 4:
            print(f"[{baris},{kolom}]", end="")
            kolom += 1
        print()
        baris += 1

def bariskolom_for():
    for baris in range(1,4):
        for kolom in range(1,4):
            print(f"[{baris},{kolom}]", end="")
        print()

def prima_while():
    batas = int(input("Masukkan batas angkat yang ingin dimunculkan = "))
    i = 2
    while i < batas:
        j = 2
        while j < i:
            # print(f"{i}%{j}={i % j}")
            if i%j == 0:
                break
            j += 1
        else:
            print(f"{i} adalah prima")
        i += 1

def prima_for():
    batas = int(input("Masukkan batas angkat yang ingin dimunculkan = "))
    for i in range(2, batas):
        for j in range(2, i):
            # print(f"{i}%{j}={i % j}")
            if i%j == 0:
                break
        else:
            print(f"{i} adalah prima")

if __name__ == '__main__':
    # dipanggil ketika file ini langsunng dijalankan
    bariskolom_while()
else:
    # dipanggil ketika file ini diimport
    print("=====PRAKTIKUM 5: Perulangan Bersarang======")