
def subsets(nums):
    result = []
    stack = []
    def tracking(nums, length):
        if len(stack) == length:
            result.append(list(stack))
            return
        for index, i in enumerate(nums):
            stack.append(i)
            temp = list(nums[index+1:])
            tracking(temp, length)
            stack.pop()

    for i in range(len(nums)):
        tracking(nums, i)
    result.append(nums)
    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(subsets(nums))




