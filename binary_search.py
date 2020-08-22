# Binary Search Algorithm
# O(log n)

def binary_search(arr, item):
    """
    Takes a sorted list of items and an item to look for
    Reeturns the index of the item in the list or none if not found
    """

    low = 0 # Frst index
    high = len(arr) - 1 # Last index

    while low <= high:
        mid = (low + high)// 2 # Middle index

        guess = arr[mid]

        # Check if item in middle index
        if guess == item:
            return mid
        
        # Otherwise, determine if we should look at the 
        # beggining or end of the list on the next pass
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None