def login():
    username = input("Masukan username = ")

    if username == "asd":
        password = input("Masukan password = ")
        if password == "123":
            print("=====WELCOME TO PRAKTIKUM ASD 1D=====")
            print(f'INDEX PRAKTIKUM: \n1. Introduction \n2. Calculator \n3. BMI')
            index = input("Masukan index menu = ")

            if index == "1":
                # import introduction as l
                # l.introduction2()
                exec(open("introduction.py").read())
            elif index == "2":
                import calculator as c
                c.simple_calculator()
            elif index == "3":
                import bmi as b
                b.conditional_bmi()
            else:
                print("ERROR MSG: Index on found")
        else:
            print("salah password")
    else:
        print("bukan admin")
    return

if __name__ == '__main__':
    # dieksekusi waktu dijalankan langsung
    login()
