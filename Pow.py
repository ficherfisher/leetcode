"""
本题的方法被称为「快速幂算法」，有递归和迭代两个版本。这篇题解会从递归版本的开始讲起，再逐步引出迭代的版本。
当指数 nn 为负数时，我们可以计算 x^−n
再取倒数得到结果，因此我们只需要考虑 nn 为自然数的情况。

我们把这些贡献相乘，x \times x^4 \times x^8 \times x^{64}x×x
4
 ×x
8
 ×x
64
  恰好等于 x^{77}x
77
 。而这些贡献的指数部分又是什么呢？它们都是 22 的幂次，这是因为每个额外乘的 xx 在之后都会被平方若干次。而这些指数 11，44，88 和 6464，恰好就对应了 7777 的二进制表示 (1001101)_2(1001101)
2
  中的每个 11！

"""

def MyPow(x, n):
    temp_a = abs(n)
    bin_n = bin(temp_a).replace("0b", "")
    count = 1
    result = 1.0
    for i in bin_n[::-1]:
        if i != "0":
            temp = track(x, count, 1)
            result = temp * result
        count *= 2
    if n <= 0:
        return 1/result
    return result

def track(x, count, i):
    a = x
    if count == i:
        return a
    a = x * x
    return track(a, count, i * 2)


if __name__ == "__main__":
    x = 2.00000
    n = 10
    print(MyPow(x, n))

