from stack_custom import Tumpukan

stack = Tumpukan()

print("Stack init = ", stack)
print("Stack isi = ", stack.tampilkan())

stack.tambah("a")
stack.tambah("b")
stack.tambah("c")

print("Isian stack = ", stack.tampilkan())
print("Paling pucuk = ", stack.ujung())

print("Ambil pucuk = ", stack.ambil())
print("Paling pucuk = ", stack.ujung())


print("Apakah kosong = ", stack.cekkosong())
print("Isian stack = ", stack.tampilkan())


