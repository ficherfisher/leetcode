
def search(nums, target):
    if nums[0] == target and len(nums) == 1: return 0
    if nums[0] != target and len(nums) == 1: return -1
    i = 0
    j = 1
    length = len(nums)
    for index in nums[:-1]:
        if nums[i] > nums[j]:
            break
        else:
            i += 1
            j += 1
    if target == nums[0]: return 0
    if target > nums[0]:
        head = 0
        end = i
    else:
        head = j
        end = length
    while True:
        mid = (head + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            end = mid
        else:
            head = mid
        if head >= end:
            return -1


if __name__ == "__main__":
    nums = [1, 3]
    target = 3
    print(search(nums, target))

