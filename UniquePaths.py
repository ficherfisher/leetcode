
def uniquePaths(m, n):
    i = m
    j = n
    hashtable = dict()
    hashtable["11"] = 1
    def tracking(row, col):
        if row < 0 or col < 0 : return 0
        if str(row)+str(col) in hashtable:
            return hashtable[str(row)+str(col)]
        temp1 = tracking(row - 1, col)
        temp2 = tracking(row, col - 1)
        hashtable[str(row)+str(col)] = temp1 + temp2
        return temp2 + temp1
    return tracking(i, j)


if __name__ == "__main__":
    m = 200
    n = 200
    import time
    StartTime = time.time()
    print(uniquePaths(m, n))
    print(time.time() - StartTime)



