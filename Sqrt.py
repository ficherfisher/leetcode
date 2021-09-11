# 二分查找

def mySqrt(x):
    i = 0
    j = x
    while True:
        mid = (i + j) // 2
        if i >= mid: return i
        if mid * mid == x: return mid
        if mid * mid > x: j = mid
        if mid * mid < x: i = mid


if __name__ == "__main__":
    x = 80
    print(mySqrt(x))

