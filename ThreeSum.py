
def threeSum(nums):
    if len(nums) <= 2: return []
    operate_nums = sorted(nums)
    length = len(operate_nums)
    for i in range(length):
        for j in range(i+1, length):
            pass
        pass



if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    print(threeSum(nums))



