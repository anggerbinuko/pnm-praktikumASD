def bubbleSortOri(arr):
    n = len(arr)
    print(f"jumlah item/panjang list = {n}")
    # Traverse through all array elements
    for i in range(n):
        print(f"= index i = {i}")
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            print(f"  == index j = {j} | arr[j] > arr[j+1] = {arr[j]} > {arr[j+1]}")
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                # a , b = b , a
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            print(f"        {arr}")


    print(f"akhirnya = {arr}")


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubbleSortDesc(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array




# Driver code to test above
if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]

    print(f"Usorted array is: {arr}")
    print(f"Sorted array is: {bubbleSort(arr)}")
    print(f"Sorted desc array is: {bubbleSortDesc(arr)}")