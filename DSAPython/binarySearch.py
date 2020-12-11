def binary_search(arr, key):
    low = 0
    high = len(arr) -1

    while high >= low:
        mid = int((high + low) / 2)
        if (key < arr[mid]):
            high = mid - 1
        elif key == arr[mid]:
            return mid
        else:
            low = mid + 1    

    return -low -1

arr = ['a', 'b', 'c', 'd', 'e', 'f']
print("The index of element c is " + str(binary_search(arr, 'g')))           