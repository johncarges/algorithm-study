
def count_islands(grid):
    visited = set()
    count = 0
    
    def explore_island(loc):
        """assumes loc is Land"""
        
        # right
        if len(grid[0]) > loc[1]+1 and (loc[0],loc[1]+1) not in visited:
            visited.add((loc[0],loc[1]+1))
            if grid[loc[0]][loc[1]+1] == 'l':
                explore_island((loc[0],loc[1]+1))
        
        # left
        if loc[1] > 0 and (loc[0],loc[1]-1) not in visited:
            visited.add((loc[0],loc[1]-1))
            if grid[loc[0]][loc[1]-1] == 'l':
                explore_island((loc[0],loc[1]-1))
        
        # up
        if loc[0] > 0 and (loc[0]-1,loc[1]) not in visited:
            visited.add((loc[0]-1,loc[1]))
            if grid[loc[0]-1][loc[1]] == 'l':
                explore_island((loc[0]-1, loc[1]))
        #down

        if len(grid) > loc[0]+1 and (loc[0]+1,loc[1]) not in visited:
            visited.add((loc[0]+1,loc[1]))
            if grid[loc[0]+1][loc[1]] == 'l':
                explore_island((loc[0]+1, loc[1]))
                
        
    for i, row  in enumerate(grid):
        for j, val in enumerate(row):
            if (i,j) in visited:
                continue
            
            visited.add((i,j))
            
            if val == 'l':
                count += 1
                print((i,j))
                explore_island((i,j))

    return count


grid = [
    ['w','l','w','w','w'],
    ['w','l','w','w','w'],
    ['w','w','w','l','w'],
    ['w','w','l','l','w'],
    ['l','w','w','l','l'],
    ['l','l','w','w','w']
]

print(count_islands(grid))

# a = [(i,j) for i in range(len(grid[0])) for j in range(len(grid)) if grid[j][i]=='w']
# print(a)




# Video way ( timestamp 1:56)

def explore(grid, r, c, visited):
    if r not in range(0,len(grid)) or c not in range(0,len(grid[0])):
        return False
    
    if grid[r][c] == 'w':
        return False
    
    if (r,c) in visited:
        return False
    
    visited.add((r,c))
    
    explore(grid, r+1, c, visited)
    explore(grid, r-1, c, visited)
    explore(grid, r, c+1, visited)
    explore(grid, r, c-1, visited)
    
    return True

def count_islands2(grid):
    visited = set()
    count = 0

    for i, row  in enumerate(grid):
        for j, val in enumerate(row):
            if explore(grid, i, j, visited):
                count += 1
            
    return count

print(count_islands2(grid))