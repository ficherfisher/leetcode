
def mergeKList(lists):
    n = len(lists)
    if n <= 1: return lists
    mid = n // 2
    left = lists[:mid]
    right = lists[mid:]
    mergeKList(left)
    mergeKList(right)
    return merge(left, right)

def merge(lefts, rights):
    result = []
    left = lefts[0]
    right = rights[0]
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    del lefts
    del rights
    return [result]


if __name__ == "__main__":
    lists = [[1,4,5],[1,3,4],[2,6]]
    print(mergeKList(lists))


