arr = [2, 3, 4, 10, 40]
x = 10

def search(arr, x):
    for i in range(0, len(arr)):
        if (arr[i] == x):
            return i

print(f"nilai {x} pada list {arr} ditemukann di index ke-{search(arr,x)}")
