def insert(intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort()
    res = []
    for s, e in intervals:
        if len(res) == 0 or res[-1][1] < s:
            res.append([s, e])
        else:
            res[-1][1] = max(res[-1][1], e)
    return res


if __name__ == "__main__":
    intervals = [[1, 2], [3, 5], [6, 7], [6, 10], [12, 16]]
    newInterval = [4, 8]
    print(insert(intervals, newInterval))



