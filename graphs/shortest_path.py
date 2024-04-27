

def shortest_path(graph,src,dst):
    visited = {src}
    queue = [src]
    distance = 0
    while len(queue)> 0:
        temp_queue = []
        for node in queue:
            for neighbor in graph[node]:
                if neighbor == dst:
                    return distance +1
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                temp_queue += neighbor
        distance +=1
        queue = temp_queue
    
    return -1

def shortest_path2(graph,src,dst):
    visited = {src}
    queue = [ [src, 0] ]

    while len(queue) > 0:
        [current, distance] = queue.pop(0)

        if current == dst:
            return distance
        
        for node in graph[current]:
            if node not in visited:
                queue.append([node, distance+1])
                visited.add(node)
    return -1


graph = {
    'a': ['b','c'],
    'b': ['a','d'],
    'c': ['a','e'],
    'd': ['b','f'],
    'e': ['c'],
    'f': ['d'],
    'g': ['h'],
    'h': ['g']
}


print(shortest_path2(graph,'a','f'))
print(shortest_path2(graph,'a','g'))