# 在数组中找x + y = target，输出x, y的下标
# 遍历数组通过字典记录x， 同时查询hash值查找字典中有无target - x


def twoSum(nums, target):
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[num] = i
    return []

if __name__ == '__main__':
    nums = [10, 1, 2, 3, 5, 6, 7, 11, 15]
    # target = 16
    # print(twoSum(nums, target))
    newNums = nums.insert(0, -1000)
    print(nums, "\n", newNums)

