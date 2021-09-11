
def countQuardruplets(nums):
    if len(nums) == 4 and sum(nums[:3]) == nums[3]: return 1
    if len(nums) == 4 and sum(nums[:3]) != nums[3]: return 0
    count = 0

    for i in range(3, len(nums)):
        for a in range(0, i):
            for b in range(a+1, i):
                for c in range(b+1, i):
                    if nums[a] + nums[b] + nums[c] == nums[i]: count += 1
    return count


if __name__ == "__main__":
    nums = [1,1,1,3,5]
    print(countQuardruplets(nums))




