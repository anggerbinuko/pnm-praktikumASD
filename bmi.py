def welcome_bmi():
    print("======WELCOME TO BODY MASS INDEX CALCULATOR======")

def calculator_bmi():
    welcome_bmi()
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

conditional_bmi()
