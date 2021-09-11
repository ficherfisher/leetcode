
def removeDuplicates(nums):
    i = 0
    j = 1
    while True:
        if j >= len(nums): return j
        if nums[i] == nums[j]:
            del nums[j]
        else:
            i = j
            j = j + 1


if __name__ == "__main__":
    nums = [-1, -1, -1, 0, 1, 2, 2, 2, 2, 3, 4]
    removeDuplicates(nums)


