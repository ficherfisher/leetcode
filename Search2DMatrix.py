
def searchMatrix(matrix, target):
    m = len(matrix) - 1
    n = len(matrix[0]) - 1
    i = 0
    j = m
    while True:
        if i >= j: break
        if matrix[i][n] == target or matrix[j][n] == target: return True
        else:
            mid = (i + j) // 2
            if matrix[mid][n] == target: return True
            if matrix[mid][n] > target: j = mid
            else: i = mid + 1
        if i >= j: break
    point = i
    i = 0
    j = n
    while True:
        if i >= j: break
        if matrix[point][i] == target or matrix[point][j] == target: return True
        else:
            mid = (i + j) // 2
            if matrix[point][mid] == target: return True
            if matrix[point][mid] > target: j = mid
            else: i = mid + 1

    return False



if __name__ == "__main__":
    matrix = [[1]]
    target = 2
    print(searchMatrix(matrix, target))

