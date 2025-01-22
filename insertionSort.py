"""
compares an element with all previous elements
then inserts at desired place. then pick the next element

key = current element
"""

def insertion_sort(arr):
    #traverse from 1 to len of the array
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr  = [12, 11, 13, 5, 6]
print("Original array:", arr)

insertion_sort(arr)
print("Sorted array:", arr)
