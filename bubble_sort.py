# Python program for implementation of Bubble Sort

def bubbleSort(arr):
    n = len(arr)
    # print(f"n = {n}")
    # Traverse through all array elements
    for i in range(n):
        # print(f"==i = {i}==")
        # Last i elements are already in place
        for j in range(n - i - 1):
            # print(f"  ==j = {j}== || arr[j] > arr[j + 1] = {arr[j]} > {arr[j + 1]}")
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] < arr[j + 1]:
                # a, b = b, a
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # print(f"  array = {arr}")

    return arr

# Driver code to test above
if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    print(f"Unsorted array is: {arr}")
    print(f"Sorted array is: {bubbleSort(arr)}")