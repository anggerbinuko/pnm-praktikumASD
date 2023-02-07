# Fungsi introduction fix variabel
def introduction(name,age,gender):
    print(f'Hi, {name}')
    print("Anda seorang",gender,"berusia",age)
    return

# Fungsi introduction2 dynamic input
def introduction2():
    name = str(input("Masukkan Nama : "))
    age = int(input("Masukkan Usia : "))
    gender = str(input("Masukkan Jenis Kelamin : "))

    # print("Hello", name)
    print(f'Hello {name}, Anda seorang {gender} dan berusia {age}')
    return

# Fungsi introduction fix variabel with control flow
def introduction3(name,age,gender):
    if gender == "pria":
        print(f'Hi mas, {name}')
    else:
        print(f'Hi mbak, {name}')
    print("Anda seorang", gender, "berusia", age)
    return

if __name__ == '__main__':
    # dipanggil ketika file ini langsunng dijalankan
    introduction('Angger', 31, "pria")
    introduction2()
    introduction3()
else:
    # dipanggil ketika file ini diimport
    print("=====PRAKTIKUM 1: Introduction (variable, data type & function)======")
    introduction2()

