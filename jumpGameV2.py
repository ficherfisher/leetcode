
def jump(nums):
    position = len(nums) - 1
    steps = 0
    while position > 0:
        for i in range(position):
            if i + nums[i] >= position:
                position = i
                steps += 1
                break;
    return steps


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(jump(nums))
