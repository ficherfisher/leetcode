# 二分法实现logN时间消耗

def searchRange(nums, target):
    i = 0
    j = len(nums) - 1
    result = []
    while True:
        if i >= j: break
        if nums[i] == target: result.append(i)
        if nums[j] == target: result.append(j)
        mid = (i + j) // 2
        if nums[mid] == target: result.append(mid)
        if nums[mid] > target: j = mid - 1
        if nums[mid] < target: i = mid + 1
    if len(result) == 0:
        return [-1, -1]
    else:return result


if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    print(searchRange(nums, target))
