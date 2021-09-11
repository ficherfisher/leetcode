
def maxSubarray(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + max(nums[i - 1], 0)
    return max(nums)


if __name__ == "__main__":
    nums = [-2,-1,-3,-4,1,-2,-1,-5,-4]
    print(maxSubarray(nums))


