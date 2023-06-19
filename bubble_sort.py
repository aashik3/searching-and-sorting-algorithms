def bubble_sort(arr):
    """
    Sort the list using the bubble sort algorithm.
    """
    n = len(arr)

    for i in range(n - 1):
        # Flag to check if any swaps were made in the current pass
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps were made in the current pass, the list is already sorted
        if not swapped:
            break

# Test the bubble sort function
my_list = [5, 2, 8, 1, 6, 3, 7, 4]
print("Original list:", my_list)

bubble_sort(my_list)
print("Sorted list:", my_list)
