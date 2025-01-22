#iterative search

def binary_search_iterative(arr, target):
    """
        arr = a sorted list of elements
        target = element to search for

        returns:
            int: The index of target if found, else -1
    """

    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2 #find the middle index
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  #target not found

#recursive binary search

def binary_search_recursive(arr, target, left, right):
    """
        arr(list): a sorted list of elements.
        target: the element to search for
        left(int): the starting index
        right(int): the ending index

        returns int: the index of target if found
    """

    if left > right:
        return -1  #target not found
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


#example iterative binary search
arr = [1,3,5,7,9,11,13,15]
target = 7

result = binary_search_iterative(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

#recursive binary search
result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
