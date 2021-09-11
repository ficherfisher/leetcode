
def insertBits(N, M, i, j):
    if N < M:
        return M
    bin_N = bin(N).replace("0b", "")
    bin_M = bin(M).replace("0b", "")
    new_bin_M = bin_M.zfill(j - i + 1)
    new_bin_N = bin_N.zfill(j + 1)
    bin_M = list(new_bin_M)[::-1]
    bin_N = list(new_bin_N)
    temp = bin_N[::-1]
    numbers = [s for s in range(i, j + 1)]
    for index, count in enumerate(numbers):
        temp[count] = bin_M[index]
    str = ""
    for s in temp[::-1]:
        str = str + s
    return int(str, 2)


if __name__ == "__main__":
    # print(insertBits(1143207437, 1017033, 11, 31))
    print(insertBits(1024, 19, 2, 6))


