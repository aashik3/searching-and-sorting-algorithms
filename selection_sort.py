def selection_sort(arr):
    """
    Sort the list using the selection sort algorithm.
    """
    n = len(arr)

    for i in range(n - 1):
        # Find the minimum element in the unsorted part of the list
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Test the selection sort function
my_list = [5, 2, 8, 1, 6, 3, 7, 4]
print("Original list:", my_list)

selection_sort(my_list)
print("Sorted list:", my_list)
