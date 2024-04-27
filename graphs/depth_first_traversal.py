"""
For bidirectional graphs (graph[a] contains b iff graph[b] contains a)
"""

def loop_depth_first_print(graph, src):
    stack = [src]
    visited = {src}

    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            if neighbor in visited:
                continue
            else:
                stack.append(neighbor)
                visited.add(neighbor)

def loop_depth_first_print_linked(graph,src):
    class Node:
        def __init__(self,val, next=None):
            self.val = val
            self.next = next
    
    class LinkedList:
        def __init__(self,head):
            self.head = head
    
        def pop(self):
            val = self.head.val
            self.head = self.head.next
            return val

        def append(self, val):
            new_head = Node(val, self.head)
            self.head = new_head
    
    stack = LinkedList(Node(val=src))
    visited = {src}

    while stack.head:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            if neighbor in visited:
                continue
            else:
                stack.append(neighbor)
                visited.add(neighbor)

def loop_has_path(graph, src, dst):
    
    visited = set(src)
    stack = [src]
    while len(stack) > 0:
        current = stack.pop(0)
        if current == dst:
            return True
        stack += [neighbor for neighbor in graph[current] if neighbor not in visited]
    return False



def recursive_depth_first_print(graph, src, visited=set()):
    print(src)
    visited.add(src)
    for neighbor in graph[src]:
        if neighbor in visited:
            continue
        recursive_depth_first_print(graph, neighbor, visited)

def recursive_has_path(graph,src, dst, visited=set()):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)
    for neighbor in graph[src]:
        if recursive_has_path(graph, neighbor, dst, visited):
            return True
    
    return False


graph = {
    'a': ['b','c'],
    'b': ['a','d'],
    'c': ['a','e'],
    'd': ['b','f'],
    'e': ['c'],
    'f': ['d']
}

loop_depth_first_print(graph, 'a')
print('')
loop_depth_first_print_linked(graph, 'a')
print('')
print(loop_has_path(graph,'a','f'))
print('')
recursive_depth_first_print(graph, 'a')
print('')
print(recursive_has_path(graph, 'a','f'))