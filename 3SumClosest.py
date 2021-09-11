# two point + order(sorted)

def threeSumClosest(nums, target):
    sortList = sorted(nums)
    length = len(sortList) - 1
    compare = 10001
    result = 0
    for index, a in enumerate(sortList):
        headPoint = index + 1
        endPoint = length
        for i in range(headPoint, endPoint):
            temp = abs(a + sortList[headPoint] + sortList[endPoint] - target)
            if temp < compare:
                compare = temp
                result = a + sortList[headPoint] + sortList[endPoint]
            if a + sortList[headPoint] + sortList[endPoint] < target:
                headPoint = headPoint + 1
            elif a + sortList[headPoint] + sortList[endPoint] > target:
                endPoint = endPoint - 1
            elif a + sortList[headPoint] + sortList[endPoint] == target:
                return target
    return result


if __name__ == "__main__":
    sortList = [-1,2,1,-4]
    target = 1
    print(threeSumClosest(sortList, target))


