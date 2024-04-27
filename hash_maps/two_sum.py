
def two_sum(arr: list[int], target: int) -> tuple[int]:
    """return indices of two numbers in arr such that their sum is target
        assume existence, uniqueness
    """

    visited = {}
    for index, num in enumerate(arr):
        if target - num in visited:
            return (visited[target-num], index)
        else:
            visited[num] = index



sample = [1,3,6,89,13,25,36,10, 38]
target = 99

# print(two_sum(sample, target))