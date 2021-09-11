
def fib(n):
    hastable = dict()
    hastable[0] = 0
    hastable[1] = 1
    def tracking(i):
        if i in hastable:
            return hastable[i]
        else:
            temp = tracking(i-1)
            temp1 = tracking(i-2)
            hastable[i] = temp1 + temp
            return hastable[i]
    return tracking(n)


def tempFib(n):
    i = 1
    def tracking(j):
        if j == 0: return 0
        if j == 1: return 1
        else:return tracking(j-2)+tracking(j-1)
    return tracking(n)


if __name__ == "__main__":
    n = 30
    print(fib(n))



