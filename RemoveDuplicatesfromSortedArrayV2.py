
def removeDuplicates(nums):
    if len(nums) <= 2: return
    i = 0
    j = 2
    while True:
        if len(nums) <= j: break
        if nums[i] == nums[j]: nums.pop(j)
        else:
            i += 1
            j += 1


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    removeDuplicates(nums)
    print(nums)



