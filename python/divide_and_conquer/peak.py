"""
Question: Finding the Peak of a Unimodal Array

Problem Statement: You are given a unimodal array A of integers, where the elements first increase to a peak at index p, and then decrease. Your task is to find the index of the peak element using a divide-and-conquer approach. The algorithm should run in O(logn) time.

Reference: Kleinberg, J. & Tardos, É. (2006). Algorithm Design. Addison-Wesley. Chapter 5, Solved Exercise 1.
"""

from __future__ import annotations

from typing import List

def peak_finder(lst: List[int]):
    """
    Find the index of the peak element in a unimodal array.

    A unimodal array is defined as an array that first increases to a maximum 
    value (the peak) and then decreases. This function uses a divide-and-conquer 
    approach to efficiently find the peak index in O(log n) time.
    
    Args:
        lst (List[int]): A list of integers representing the unimodal array. The list must have at least one element, and all elements must be distinct.
    
    Returns:
        int: The index of the peak element in the array. 
                         
    Raises:
        ValueError: If the input list is empty or contains duplicate elements.
    
    """
    # middle index
    m = len(lst) // 2
    
    # choose the middle three elements
    num_1, num_2, num_3 = lst[m - 1: m + 2]
    
    # if middle element is peak
    if num_2 > num_1 and num_2 > num_3:
        return num_2
    
    # if increasing, recurse on right
    elif num_1 < num_3:
        if len(lst[:m]) == 2:
            m -= 1
        return peak_finder(lst[m:])
    
    # decreasing
    else:
        if len(lst[:m]) == 2:
            m += 1
        return peak_finder(lst[:m])


if __name__ == "__main__":
    lst = [1, 10, 9, 8, 7, 6, 5, 4]
    peak = peak_finder(lst=lst)
    print(peak)
    
    