
def canJump(self, nums: List[int]) -> bool:
    position = len(nums) - 1
    steps = 0
    tag = 1
    while position > 0:
        for i in range(position):
            if i + nums[i] >= position:
                position = i
                steps += 1
                tag = 0
                break;
        if tag == 1:
            return False
        else:
            tag = 1
    return True


if __name__ == "__main__":
    nums = [3,2,1,0,4]
    print(canJump(nums))

