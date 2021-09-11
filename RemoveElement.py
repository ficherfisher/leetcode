
def removeElement(nums, val):
    i = 0
    while True:
        length = len(nums)
        if i == length: return i
        if nums[i] == val:
            del nums[i]
        else:i += 1



if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    removeElement(nums, val)



