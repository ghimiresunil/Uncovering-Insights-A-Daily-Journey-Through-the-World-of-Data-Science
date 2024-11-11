from __future__ import annotations

def merge(left_half: list, right_half: list) -> list:
    """Helper function for mergesort that merges two sorted halves into a single sorted list.

    Args:
        left_half: The left half of the list, already sorted.
        right_half: The right half of the list, already sorted.

    Returns:
        A merged and sorted list of elements from left_half and right_half.
    """
    sorted_array = [None] * (len(right_half) + len(left_half))

    pointer1 = 0  # pointer to current index for left Half
    pointer2 = 0  # pointer to current index for the right Half
    index = 0  # pointer to current index for the sorted array Half

    while pointer1 < len(left_half) and pointer2 < len(right_half):
        if left_half[pointer1] < right_half[pointer2]:
            sorted_array[index] = left_half[pointer1]
            pointer1 += 1
        else:
            sorted_array[index] = right_half[pointer2]
            pointer2 += 1
        index += 1

    while pointer1 < len(left_half):
        sorted_array[index] = left_half[pointer1]
        pointer1 += 1
        index += 1

    while pointer2 < len(right_half):
        sorted_array[index] = right_half[pointer2]
        pointer2 += 1
        index += 1

    return sorted_array


def merge_sort(array: list) -> list:
    """Sorts a list of elements using the merge sort algorithm.

    Args:
        array: The list of elements to sort.

    Returns:
        A sorted list of elements.
    """
    if len(array) <= 1:
        return array
    
    middle = 0 + (len(array) - 0) // 2  # Calculating the middle element to split the array

    # Split the array into two halves and recursively sort each half
    left_half = array[:middle]
    right_half = array[middle:]

    # Merge the sorted halves
    return merge(merge_sort(left_half), merge_sort(right_half))


if __name__ == "__main__":
    # Example usage and testing the merge sort
    array = [-2, 3, -10, 11, 99, 100000, 100, -200]
    print("Sorted array:", merge_sort(array))

    array = [10000000, 1, -1111111111, 101111111112, 9000002]
    print("Sorted array:", merge_sort(array))

    array = [-200]
    print("Sorted array:", merge_sort(array))

    array = []
    print("Sorted array:", merge_sort(array))
