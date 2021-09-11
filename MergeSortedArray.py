
def merge(nums1, m, nums2, n):
    i = 0
    j = 0
    del nums1[m:]
    while n > j:
        length = len(nums1)
        if m == 0: break
        if nums1[i] >= nums2[j]:
            nums1.insert(i , nums2[j])
            i += 1
            j += 1
        else:
            i += 1
            if length <= i: break
            else:continue
    if j < n:
        while n > j:
            nums1.insert(i, nums2[j])
            i += 1
            j += 1



if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)


