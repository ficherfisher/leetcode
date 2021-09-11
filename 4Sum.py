
def fourSum(nums, target):
    sortList = sorted(nums)
    headPoint = 0
    endPoint = len(sortList) - 1
    result = []
    for index, i in enumerate(sortList):
        index1 = index + 1
        for j in sortList[index1:]:
            headPoint = index1 + 1
            for s in range(headPoint, endPoint):
                if i + j + sortList[headPoint] + sortList[endPoint] < target:
                    headPoint = headPoint + 1
                elif i + j + sortList[headPoint] + sortList[endPoint] > target:
                    endPoint = endPoint - 1
                elif i + j + sortList[headPoint] + sortList[endPoint] == target:
                    result.append([i, j, sortList[headPoint], sortList[endPoint]])
    return result


if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    print(fourSum(nums, target))


