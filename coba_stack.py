from custom_stack2 import Tumpukan

stack = Tumpukan()

print("awal = ",stack.ukuran())

stack.tambah('a')
stack.tambah('b')
stack.tambah('c')

print("isi stack = ",stack.tampilkan())

print("paling pucuk", stack.pucuk())

print("ambil", stack.akhir())
print("ambil", stack.akhir())
print("ambil", stack.akhir())

print("akhir = ",stack.ukuran())