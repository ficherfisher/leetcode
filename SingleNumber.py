"""
交换律：a ^ b ^ c <=> a ^ c ^ b
任何数于0异或为任何数 0 ^ n => n
相同的数异或为0: n ^ n => 0
var a = [2,3,2,4,4]
2 ^ 3 ^ 2 ^ 4 ^ 4等价于 2 ^ 2 ^ 4 ^ 4 ^ 3 => 0 ^ 0 ^3 => 3
"""


def singleNumber(nums):
    a = 0
    for num in nums:
        a = a ^ num
    return a


if __name__ == "__main__":
    nums = [2, 2, 1]
    print(singleNumber(nums))



