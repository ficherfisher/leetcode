
def subsetWithDup(nums):
    result = []
    stack = []
    def tracking(nums, length):
        if len(stack) == length:
            if list(stack) not in result:
                result.append(list(stack))
            return
        for index, i in enumerate(nums):
            stack.append(i)
            temp = list(nums[index + 1:])
            tracking(temp, length)
            stack.pop()

    for i in range(len(nums)):
        tracking(nums, i)
    result.append(nums)
    return result


if __name__ == "__main__":
    nums = [1, 2, 2]
    print(subsetWithDup(nums))

