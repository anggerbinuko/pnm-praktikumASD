# Define list
random = ["satu",2,3.0,True]

# Mengakses nilai dari list index ke-?
print(f"Random idx 3 sebelum di update = {random[3]}, type data = {type(random[3])}")
# Update data index dr list ranndom
random[3] = "EMPAT"
# print ulang
print(f"Random idx 3 setelah di update = {random[3]}, type data = {type(random[3])}")

# print semua list
print(f"Random = {random}")
# menghapus data pake index
del random[1]
# print ulang
print(f"Random = {random}")
# menghapus data pake nilai object
random.remove("satu")
# print ulang
print(f"Random = {random}")
# menambah data ke dalam list
random.append("lima")
# print ulang
print(f"Random = {random}")
# menyisipkan data ke dalam list
random.insert(0, 1)
# print ulang
print(f"Random = {random}")
# sisipkan lagi
random.insert(1, "dua")
# print ulang
print(f"Random = {random}")
# menghitung jumlah data dalam list
print("jumlah data Random = ", len(random))
print("jumlah data 3.0 dalam Random muncul sebanyak ", random.count(3.0))

list1 = [1,2,3]
list2 = ["empat", "lima", "enam"]
list1n2 = list1 + list2
print("Concat list 1 & list 2 = ", list1n2)

intro = ["Hello"]
intromulti = intro * 4
print("Multiple list = ", intromulti)

print('Apakah ada data "empat" di dalam list1n2? ', "empat" in list1n2)

# implementasi iterasi
for i in list1n2:
    print(f"item {i}")
for i, value in enumerate(list1n2):
    print(f"item ke-{i} isinya {value}")