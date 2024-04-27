"""
Count distinct connected sub-graphs
"""

def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore_subgraph(graph, node, visited):
            count +=1
    return count

def explore_subgraph(graph,current,visited):
    """returns True once all neighbors have been visited"""
    if current in visited:
        return False
    
    visited.add(current)

    for neighbor in graph[current]:
        explore_subgraph(graph,neighbor,visited)

    return True



graph = {
    'a': ['b','c'],
    'b': ['a','d'],
    'c': ['a',],
    'd': ['b'],
    'e': ['f'],
    'f': ['e']
}


print(connected_components_count(graph))