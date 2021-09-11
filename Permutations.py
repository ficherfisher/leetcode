
# 回溯法


def permuate(nums):
    result = []
    def tracking(temp, nums):
        if len(temp) == len(nums):
            result.append(list(temp))
            return
        for i in nums:
            if i in temp: continue
            temp.append(i)
            tracking(temp, nums)
            temp.pop()
    tracking([], nums)
    return result

if __name__ == "__main__":
    nums = [1, 2]
    print(permuate(nums))
