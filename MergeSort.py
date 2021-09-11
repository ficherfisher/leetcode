# 归并排序


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    merge_sort(left)
    merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result


if __name__ == "__main__":
    nums = [11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22]
    print(merge_sort(nums))



