

def largest_component(graph):
    largest = 0
    visited = set()

    def explore_subgraph(node):
        if node in visited:
            return 0
        visited.add(node)
        count = 1
        for neighbor in graph[node]:
            count += explore_subgraph(neighbor)
        return count
    
    for node in graph:
        if node in visited:
            continue
        largest = max(largest, explore_subgraph(node))

    return largest
    
def smallest_component(graph):
    smallest = len(graph)
    visited = set()

    def explore_subgraph(node):
        if node in visited:
            return 0
        visited.add(node)
        count = 1
        for neighbor in graph[node]:
            count += explore_subgraph(neighbor)
        return count
    
    for node in graph:
        if node in visited:
            continue
        smallest = min(smallest, explore_subgraph(node))
        

    return smallest


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

print(largest_component(graph))
print(smallest_component(graph))
"""
    1. check if node is visited
    2. if not, add 1 to current
    3. recurse on each neighbor

"""