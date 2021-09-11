
def rotate(matrix):
    n = len(matrix[0])
    temp = []
    for items in matrix:
        a = []
        for j in items:
            a.append(j)
        temp.append(a)
    for i in range(n):
        col = n - 1
        raw = i
        for j in range(n):
            matrix[i][j] = temp[col][raw]
            col -= 1



if __name__ == "__main__":
    matrix = [[1, 2], [3, 4]]
    rotate(matrix)

