
def combinationSum(candidates, target):
    result = []
    nums = sorted(candidates)
    if sum(nums) == target: return [nums]
    if sum(nums) < target: return []
    def tracking(temp, nums, target):
        if sum(temp) == target:
            if sorted(temp) not in result:
                result.append(sorted(temp))
            return
        if sum(temp) > target:
            return
        for i in nums:
            temp.append(i)
            nums.remove(i)
            Newnums = list(nums)
            tracking(temp, Newnums, target)
            nums.insert(0, i)
            temp.pop()
    tracking([], nums, target)
    return result


if __name__ == "__main__":
    candidates = [1, 2]
    target = 2
    print(combinationSum(candidates, target))



