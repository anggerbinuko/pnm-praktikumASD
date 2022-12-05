# Python program for implementation of Insertion Sort
# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)

    for i in range(1, len(arr)):
        print(f"============= phase {i} ================")
        print(f"array awal = {arr}")
        key = arr[i]
        print(f"nilai kartu yg diambil untuk dibandingkan (key) = {key}")
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        print(f"index kartu yg akan dibandingkan (j) = {j}")
        print(f"nilai kartu yg dijadikan pembanding (arr[j]) = {arr[j]}")
        print(f"maka, key < arr[j] = {key} < {arr[j]}")

        while j >= 0 and key < arr[j]:
            print(f"{j} >= 0 dan key < arr[j] = {key} < {arr[j]}, masuk trus tukar kartu pembanding dengan kartu dibanding")
            print(f"arr[j + 1]= {arr[j + 1]}")
            print(f"arr[j]= {arr[j]}")
            arr[j + 1] = arr[j]
            print(f"sudah ditukar arr[j+1]/arr[{j + 1}] = {arr[j+1]}")
            print(f"nilai sementara {arr}")
            j -= 1

        print(f"endingnya jika j udah tidak memenuhi syarat maka j+1 = {j+1}, ubah jadi key = {key}")
        arr[j + 1] = key
        print(f"array akhir = {arr}")
    return arr

# Driver code to test above
# arr = [12, 11, 13, 5, 6]
arr = [7, 8, 5, 2, 4, 6, 3]
print(f"unsorted = {arr}")
print(f"sorted = {insertionSort(arr)}")

# This code is contributed by Mohit Kumra