
def searchInsert(nums, target):
    i = 0
    j = len(nums) - 1
    while True:
        if i >= j: break
        if nums[i] == target: return i
        if nums[j] == target: return j
        mid = (i + j) // 2
        if nums[mid] == target: return mid
        if nums[mid] > target: j = mid - 1
        if nums[mid] < target: i = mid + 1
    return i + 1


if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 0
    print(searchInsert(nums, target))

