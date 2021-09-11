
"""
第n个台阶只能从第n-1或者n-2个上来。
到第n-1个台阶的走法 + 第n-2个台阶的走法 = 到第n个台阶的走法，
已经知道了第1个和第2个台阶的走法，一路加上去。
"""


def climbStairs(n):
    hashtable = dict()
    hashtable[1] = 1
    hashtable[2] = 2
    def tracking(n):
        if n in hashtable:
            return hashtable[n]
        else:
            temp = tracking(n - 1)
            temp1 = tracking(n - 2)
            hashtable[n] = temp + temp1
            return temp + temp1
    return tracking(n)



if __name__ == "__main__":
    n = 40
    print(climbStairs(n))


