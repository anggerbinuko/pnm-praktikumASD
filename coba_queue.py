from custom_queue import Antrian

queue = Antrian()

print("awal = ",queue.ukuran())

queue.tambah('a')
queue.tambah('b')
queue.tambah('c')

print("isi atrian = ",queue.tampilkan())

print("paling awal", queue.kepala())
print("paling akhir", queue.ekor())

print("ambil", queue.ambil())
print("ambil", queue.ambil())
print("ambil", queue.ambil())

print("akhir = ",queue.ukuran())