def binary_search(arr: list[int], target: int) -> int:
    """ Return Index of target 
        Assumes unique index, and target in arr
    """
    index= len(arr)//2
    candidate = arr[index]

    if candidate == target:
        return index
    elif candidate > target:
        return binary_search(arr[0:index], target)
    else:
        return binary_search(arr[index:], target)
    



print(binary_search([1,3,5,6,9,13,15,18,39,42,46,48], 3))