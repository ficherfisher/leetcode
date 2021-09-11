
def minPathSum(grid):
    dp = [[0] * len(grid[0]) for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0:
                dp[i][j] = grid[0][0]
            elif j == 0 and i != 0:
                dp[i][j] = dp[i - 1][j] + grid[i][j]
            elif i == 0 and j != 0:
                dp[i][j] = dp[i][j - 1] + grid[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[len(grid) - 1][len(grid[0]) - 1]


if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(minPathSum(grid))





