def bubble_sort(array):
    n = len(array) # jumlah list
    # perulangan pertama
    for i in range(n):
        # perulangan kedua
        for j in range(n - i - 1):
            # bandingkan masing" elemen
            if array[j] > array[j + 1]:
                # jika lebih besar, tukar.
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def selection_sort(arr):
    n = len(arr)
    # perulangan list elemen
    for i in range(n):
        # cari nilai elemen terendah
        # yang masih tersedia
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # tukar dengan nilai elemen ke-i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(array):
    # perulangan pertama
    for i in range(1, len(array)):
        # ini elemen yang akan kita posisikan
        key_item = array[i]
        # kunci index posisi
        j = i - 1
        print(f"i = {i}, key = {key_item}, j = {j}")
        # lakukan perulangan kedua
        while j >= 0 and array[j] > key_item:
            # menggeser elemen yang lain
            print(f"==asd==={array[j+1]} = {array[j]}")
            array[j + 1] = array[j]
            j -= 1
        # memposisikan elemen
        print(f"==aer==={array[j + 1]} = {key_item}")
        array[j + 1] = key_item
        print(f"======={array}")
    return array

list = [5, 3, 4, 8, 1, 2, 9, 6]
print("unsorted = ", list)
# print("buble sort = ", bubble_sort(list))
# print("selection sort = ", selection_sort(list))
print("insertion sort = ", insertion_sort(list))
