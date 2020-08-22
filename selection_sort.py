# Selection sort soting algorithm
# O(n^2)

def selection_sort(arr):
    """"
    Selection sort 
    """

    if len(arr) <= 1:
        return None

    for i in range(len(arr)):
        # Move through each index in list
        # Set current element as smallest 
        smallest = i

        # Now check the rest of the list for the smallest element 
        for j in range(i+1, len(arr)):
            # Find the smallest
            # If smaller, then swap
            if arr[j] < arr[smallest]:
                smallest = j
        
        # If we find a smaller element, swap with current element 
        arr[i], arr[smallest] = arr[smallest], arr[i]