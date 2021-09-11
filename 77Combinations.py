
def combine(n, k):
    result = []
    num = [i for i in range(1, n+1)]
    stack = []
    def tracking(nums, length):
        if len(stack) == length:
            result.append(list(stack))
            return
        for index, i in enumerate(nums):
            stack.append(i)
            temp = list(nums[index + 1:])
            tracking(temp, length)
            stack.pop()
    tracking(num, k)
    return result


if __name__ == "__main__":
    n = 3
    k = 2
    print(combine(n, k))

