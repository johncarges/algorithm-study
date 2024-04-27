def breadth_first_print(graph, src):
    queue = [src]
    visited = {src}
    while len(queue) > 0:
        current = queue[0]
        print(current)
        visited.add(current)
        queue += [neighbor for neighbor in graph[current] if neighbor not in visited]
        queue = queue[1:]




graph = {
    'a': ['b','c'],
    'b': ['a','d'],
    'c': ['a','e'],
    'd': ['b','f'],
    'e': ['c'],
    'f': ['d']
}

breadth_first_print(graph, 'a')


# With deque:

from collections import deque

def breadth_first_print2(graph, src):
    queue = deque()
    queue.append(src)

    visited = {src}

    while len(queue) > 0:
        current = queue.popleft()
        print(current)
        visited.add(current)
        queue.extend([val for val in graph[current] if val not in visited])


breadth_first_print2(graph,'a')