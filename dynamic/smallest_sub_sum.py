example = [20, -7, -3, 9 , -4, 6, -9, 10]

def min_sum_sub(arr):
    min_sum = float('inf')

    current_sum = 0

    for num in arr:
        if current_sum <= 0:
            current_sum += num
        else:
            current_sum = num
        
        min_sum = min(min_sum, current_sum)

    return min_sum

print(min_sum_sub(example))