import math

# 2147483647   # 二分法
def findPrimes(nums):
    temp = [2, 3, 5, 7]
    tag = 1
    for i in range(11, 46342, 2):
        for j in temp:
            if i % j == 0:
                tag = 0
                break
            if math.sqrt(i) < j: break
        if tag != 0:
            temp.append(i)
        tag = 1
    temp2 = [i * i for i in temp]
    for i in temp2:
        if nums / i in temp2 or nums / i == 1:
            return True
        if nums < i:
            return False
    return False


if __name__ == "__main__":
    print(findPrimes(2147117569))





