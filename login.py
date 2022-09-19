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
    # exec(open("introduction.py").read())
    import introduction as i
    i.introduction2()
