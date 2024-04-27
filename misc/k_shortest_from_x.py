import bisect

def k_shortest(arr: list[int], target: int, k: int) -> list[int]:

    ans = sorted(arr[:7], key= lambda x: abs(x-target))

    for val in arr[k:]:
        if abs(val-target) < abs(arr[k] - target):
            bisect.insort(arr, val)
    
    return ans[:k]



sample = [1,13,6,83,22,44,5,23,14,2]
target = 9
k = 4

print(k_shortest(sample, target, k))

