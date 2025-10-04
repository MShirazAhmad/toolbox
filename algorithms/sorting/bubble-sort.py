"""
Bubble Sort Algorithm Implementation

Bubble sort is a simple sorting algorithm that repeatedly steps through
the list, compares adjacent elements and swaps them if they are in the
wrong order.
"""

def bubble_sort(arr):
    """
    Sort an array using bubble sort algorithm.
    
    Args:
        arr (list): List of comparable elements to sort
        
    Returns:
        list: Sorted list (modifies in-place and returns)
        
    Time Complexity: O(n²) - worst and average case
                     O(n) - best case (already sorted)
    Space Complexity: O(1) - sorts in place
    
    Best for: Small datasets or nearly sorted data
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Track if any swap was made in this pass
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return arr


# Usage examples:
if __name__ == "__main__":
    # Example 1: Basic usage
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {numbers}")
    sorted_numbers = bubble_sort(numbers.copy())
    print(f"Sorted array: {sorted_numbers}")
    
    # Example 2: Already sorted array (best case)
    sorted_arr = [1, 2, 3, 4, 5]
    print(f"\nAlready sorted: {sorted_arr}")
    bubble_sort(sorted_arr)
    print(f"Result: {sorted_arr}")
    
    # Example 3: Reverse sorted array (worst case)
    reverse_arr = [5, 4, 3, 2, 1]
    print(f"\nReverse sorted: {reverse_arr}")
    bubble_sort(reverse_arr)
    print(f"Result: {reverse_arr}")
