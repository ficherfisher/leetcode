"""
动态规划
假设n个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数
即有:G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)
当i为根节点时，其左子树节点个数为[1,2,3,...,i-1]，右子树节点个数为[i+1,i+2,...n]，所以当i为根节点时，其左子树节点个数为i-1个，右子树节点为n-i，即f(i) = G(i-1)*G(n-i),
上面两式可得:G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
"""


def numTrees(n):
    hashtable = dict()
    hashtable[0] = 1
    hashtable[1] = 1
    def tracking(i):
        if i in hashtable: return hashtable[i]
        else:
            temp = 0
            for a in range(i):
                temp += tracking(a) * tracking(i - a - 1)
            hashtable[i] = temp
            return temp
    return tracking(n)


if __name__ == "__main__":
    n = 120
    print(numTrees(n))


