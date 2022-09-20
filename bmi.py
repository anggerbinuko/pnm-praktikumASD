def calculator_bmi():
    tinggi = int(input("Masukkan tinggi badan:"))
    berat = int(input("Masukkan berat badan:"))
    bmi = berat / (tinggi/100) ** 2
    return bmi

def conditional_bmi():
    n = calculator_bmi()
    print("Nilai BMI Anda = %.3f" % (n))
    print(f'Nilai BMI Anda = {n:.2f}')
    if n < 18.5:
        print("BMI Anda kekurusan")
    elif 18.5 < n < 24.9:
        print("BMI Anda normal")
    elif 25 < n < 29.9:
        print("BMI Anda kegemukan")
    else:
        print("BMI Anda obesitas")
    return

if __name__ == '__main__':
    # dipanggil ketika file ini langsunng dijalankan
    calculator_bmi()
else:
    # dipanggil ketika file ini diimport
    print("=====PRAKTIKUM 3: BODY MASS INDEX CALCULATOR (operators & expressions)======")
