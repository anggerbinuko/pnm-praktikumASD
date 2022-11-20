class Tumpukan:
    def __init__(self):
        self.list = []

    def ukuran(self):
        return len(self.list)

    def tambah(self, value):
        self.list.append(value)

    def ambil(self):
        return self.list.pop()

    def tampilkan(self):
        return self.list

    def ujung(self):
        return self.list[-1]

    def cekkosong(self):
        if len(self.list) == 0:
            return True
        else:
            return False