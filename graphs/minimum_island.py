


def minimum_island(grid):
    visited = set()
    smallest = len(grid) * len(grid[0])
    size = 0

    def explore_and_size(grid, r, c, visited, size):
        """
        explore individual square and add neighboring square explore to call stack
        returns new (visited, size) after exploration
        """

        if r not in range(0,len(grid)) or c not in range(0,len(grid[0])):
            return (visited, size)
        
        if (r,c) in visited:
            return (visited, size)
        
        visited.add((r,c))
    
        if grid[r][c] == 'w':
            return (visited, size)
        
        size += 1 

        (visited, size) = explore_and_size(grid, r+1, c, visited, size)
        (visited, size) = explore_and_size(grid, r-1, c, visited, size)
        (visited, size) = explore_and_size(grid, r, c+1, visited, size)
        (visited, size) = explore_and_size(grid, r, c-1, visited, size)
        
        return (visited, size)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (current:=explore_and_size(grid, i, j,visited, size)[1]):
                smallest = min(smallest, current)
                size = 0
    return smallest




grid = [
    ['w','l','w','w','w'],
    ['w','l','l','w','w'],
    ['w','w','w','l','w'],
    ['w','w','l','l','w'],
    ['l','w','w','l','l'],
    ['l','l','w','w','w']
]


print(minimum_island(grid))