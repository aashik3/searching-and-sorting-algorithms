def linear_search(arr, target):
    """
    Perform linear search to find the target element in the list.
    Return the index if found, else return -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Test the linear search function
my_list = [4, 2, 9, 7, 5, 1, 8, 3, 6]
target_element = 5

result = linear_search(my_list, target_element)
if result != -1:
    print("Element", target_element, "found at index", result)
else:
    print("Element", target_element, "not found in the list.")
