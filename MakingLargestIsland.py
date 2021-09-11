res = 0
max = 0

def largestIsland(grid):
    n = len(grid[0])
    temp = [1, 2]
    temp[0] = grid
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0: grid[i][j] = 1
            MostDalianTongBlock(grid, n)
            grid = temp[0]


def MostDalianTongBlock(grid, n):
    global max
    global res
    for i in range(n):
        for j in range(n):
            dfs(grid, i, j, n)
            if res > max: max = res
            res = 0

def dfs(grid, i, j, n):
    global res
    if i<0 or i>n-1 or j<0 or j>n-1 or grid[i][j] == 0: return
    grid[i][j] = 0
    res = res + 1
    dfs(grid, i, j+1, n)
    dfs(grid, i, j-1, n)
    dfs(grid, i+1, j, n)
    dfs(grid, i-1, j, n)
    return grid


if __name__ == '__main__':
    grid = [[0, 0, 1], [1, 1, 1], [0, 0, 1]]
    largestIsland(grid)
    print(max)



