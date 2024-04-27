import heapq

minHeap = []

heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 1)
heapq.heappush(minHeap, 6)

print(minHeap)

while len(minHeap):
    print(heapq.heappop(minHeap))
    

