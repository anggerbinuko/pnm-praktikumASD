def counter_angka_while(n):
    count = 0
    while count < n:
        print(f'angka {count+1}')
        count += 1
    else:
        print("selesai")

def counter_angka_for(n):
    for i in range(0, n):
        print(f'angka {i+1}')
    print("selesai")

def counter_angkaganjil_while(n):
    count = 1
    while count <= n:
        if count % 2 == 1:
            print(f'angka {count}')
        count += 1
    else:
        print("selesai")

def counter_angkafgenap_for(n):
    for i in range(0, n):
        if i % 2 == 0:
            if i == 0:
                pass
            else:
                print(f'angka {i}')
    print("selesai")

def nestedloop_prime_while():
    i = 2
    while (i < 20):
        j = 2
        while (j <= (i / j)):
            if not (i % j):
                break
            j = j + 1

        if (j > i / j):
            print(i, " is prime")

        i = i + 1

def nestedloop_prime_while2():
    i = 2
    while (i < 20):
        j = 2
        while (j < i):
            if i % j == 0:
                break
            j = j + 1
        else:
            print("angka i =", i)
        i = i + 1

def nestedloop_prime_for():
    for i in range(2, 10):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i, " is prime")

def counter_totalangkaganjil_while(n):
    count = 1
    jumlah = 0
    while count <= n:
        if count % 2 == 1:
            print(f'angka {count}')
            jumlah += count
        count += 1
    else:
        print("Total penjumlahan = ", jumlah)

def counter_totalangkagenap_for(n):
    jumlah = 0
    for i in range(0, n):
        if i % 2 == 0:
            if i == 0:
                pass
            else:
                jumlah += i
                print(f'angka {i}')
    print("Total penjumlahan = ", jumlah)

def counter_break():
    for i in range(0, 20):
        print(f'angka = {i}')
        if i == 3:
            break

def string_break():
    print("=========break==========")
    for i in "angger":
        if i == 'g':
            break
        print(f'huruf = {i}')


def string_pass():
    print("=========pass==========")
    for i in "angger":
        if i == 'g':
            pass
        print(f'huruf = {i}')

def string_continue():
    print("=========continue==========")
    for i in "angger":
        if i == 'g':
            continue
        print(f'huruf = {i}')

def counter_continue():
    print("=========continue==========")
    for i in range(0,10):
        if i%2 :
            continue
        print(f'angka = {i}')

# panggil fungsi
# counter_angka_while(5)
# counter_angka_for(5)
# counter_angkaganjil_while(20)
# counter_angkafgenap_for(10)
# nestedloop_prime_while()
# nestedloop_prime_while2()
# nestedloop_prime_for()
# counter_totalangkaganjil_while(10)
# counter_totalangkagenap_for(10)
# counter_break()
# string_break()
# string_pass()
# string_continue()
counter_continue()
