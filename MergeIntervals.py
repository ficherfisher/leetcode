def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    res = []
    for s, e in intervals:
        if len(res) == 0 or res[-1][1] < s:
            res.append([s, e])
        else:
            res[-1][1] = max(res[-1][1], e)
    return res


if __name__ == "__main__":
    intervals = [[[2,3],[4,5],[6,7],[8,9],[1,10]]]
    print(sorted(intervals))
    # print(merge(intervals))


