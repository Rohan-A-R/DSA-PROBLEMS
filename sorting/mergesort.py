def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle index
        left_half = arr[:mid]  # Divide the array into left half
        right_half = arr[mid:]  # Divide the array into right half

        merge_sort(left_half)  # Recursively sort left half
        merge_sort(right_half)  # Recursively sort right half

        # Merge the sorted halves
        merge(arr, left_half, right_half)

def merge(arr, left_half, right_half):
    i = j = k = 0  # Pointers for left, right, and merged array

    # Merge left and right halves
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Copy remaining elements of left_half (if any)
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Copy remaining elements of right_half (if any)
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Example Usage
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted Array:", arr)




def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Step 1: Divide
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Step 2: Merge
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    # Append remaining elements
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

# Example usage
arr = [9, 3, 7, 5, 6, 4, 8, 2]
sorted_arr = merge_sort(arr)
print(sorted_arr)
