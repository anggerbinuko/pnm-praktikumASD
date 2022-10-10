# Define list
#random = ("satu",2,3.0,True)
# Mengakses nilai dari list index ke-?
#print(f"Tuple random idx 3 sebelum di update = {random[3]}, type data = {type(random[3])}")
# Update data index dr list ranndom
#random[3] = "EMPAT"
#del random
# Mengakses nilai dari list index ke-?
#print(f"Random idx 3 sebelum di update = {random[3]}, type data = {type(random[3])}")


list1 = [1,2,3,4,5,1,2,3,4,5]
set1 = {1,2,3,4,5}

print(f"List 1 = {list1}")
print(f"Set 1 = {set1}")
set1.add(6)
print(f"Set 1 = {set1}")

for i in range(0, len(set1)):
    if i == 3:
        set1.add("empat")
    print(i)
print(f"Set 1 = {set1}")

print("List diubah ke set", set(list1))

