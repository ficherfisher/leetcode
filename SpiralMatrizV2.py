
def generateMatrix(n):
    if n == 1: return [[1]]
    result = []
    visited = []
    for i in range(n):
        temp = []
        temp1 = []
        for j in range(n):
            temp.append(0)
            temp1.append(False)
        result.append(temp)
        visited.append(temp1)
    col, row = 0, 0
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 右、下、左、上
    directionIndex = 0
    for i in range(1, n*n+1):
        result[col][row] = i
        visited[col][row] = True
        nextCol, nextRow= col + directions[directionIndex][0], row + directions[directionIndex][1]
        if not (0 <= nextRow < n and 0 <= nextCol < n and not visited[nextCol][nextRow]):
            directionIndex = (directionIndex + 1) % 4
        col += directions[directionIndex][0]
        row += directions[directionIndex][1]
    return result


if __name__ == "__main__":
    n = 3
    print(generateMatrix(n))

