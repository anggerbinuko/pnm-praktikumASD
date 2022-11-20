from queue_custom import Antrian

queue = Antrian()

print("queue init = ", queue)
print("queue isi = ", queue.tampilkan())

queue.tambah("a")
queue.tambah("b")
queue.tambah("c")
queue.tambah("d")
queue.tambah("e")
queue.tambah("f")

print("Lihat antriann = ", queue.tampilkan())
print("Antrian depan", queue.depan())
print("Antrian tengah", queue.tengah())
print("Antrian belakang", queue.belakang())

print("Antrian depan maju", queue.ambil())
print("Lihat antriann = ", queue.tampilkan())

ndiambil = queue.ambil()

print("Lihat antriann = ", queue.tampilkan())

queue.tambah(ndiambil)

print("Lihat antriann = ", queue.tampilkan())