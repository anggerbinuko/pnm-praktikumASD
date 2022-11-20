class Antrian:
    def __init__(self):
        self.q = []

    def ambilindex(self,value):
        # return self.q[value]
        return self.q.pop(value)


    def ukuran(self):
        return len(self.q)

    def tambah(self, value):
        self.q.append(value)

    def ambil(self):
        return self.q.pop(0)

    def tampilkan(self):
        return self.q

    def depan(self):
        return self.q[0]

    def belakang(self):
        return self.q[-1]

    def tengah(self):
        t = (len(self.q)-1)/2
        print("nilai tenngah", round(t))
        return self.q[round(t)]

    def cekkosong(self):
        if len(self.q) == 0:
            return True
        else:
            return False