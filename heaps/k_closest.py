import heapq

def k_closest(points: list[tuple[int]], target: list[int], k: int) -> list[tuple[int]]:
    minHeap = []

    for x, y in points:
        dist = (x**2) + (y**2)
        minHeap.append((dist, x, y))

    heapq.heapify(minHeap)
    ans = []
    while k > 0:
        dist, x, y, = heapq.heappop(minHeap)
        ans.append((x,y))
        k -= 1 