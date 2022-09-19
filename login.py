def login():
    username = input("Masukkan username = ")

    if username == "asd":
        password = input("Masukkan password = ")
        if password == "123":
            # print("masuk sistem")
            welcome_to_sistem()
        else:
            print("salah pasword")
    else:
        print("bukan admin")

def welcome_to_sistem():
    print("=====WELCOME TO SYSTEM======")
    print("=====INDEX latihan Praktikum======")
    print("1. Introduction \n2. Calculator \n3. BMI")
    # exec(open("introduction.py").read())
    index = input("Masukan index latihan = ")
    if index == "1":
        exec(open('introduction.py').read())
    elif index == "2":
        import calculator as c
        c.simple_calculator()
    elif index == "3":
        import bmi
        bmi.conditional_bmi()
    else:
        print("Index tidak tersedia")

