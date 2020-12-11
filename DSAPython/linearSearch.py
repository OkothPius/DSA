def linear_Search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i 
    return -1

arr = ['a', 'b', 'c', 'd', 'e']
print("The index of element c is " + str(linear_Search(arr, 'c')))            