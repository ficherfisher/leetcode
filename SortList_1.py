
def sort(nums):
    if len(nums) <= 1: return nums
    mid = len(nums) // 2
    left = sort(nums[:mid])
    right = sort(nums[mid:])
    return merge(left, right)



def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    result += left
    result += right
    return result


if __name__ == "__main__":
    nums = [-1,5,3,4]
    for j, i in zip(nums, reversed(nums)):
        print(i, j)
    print(sort(nums))


