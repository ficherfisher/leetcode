

def combinationSum(k, n):
    result = []
    tag = 1
    numbers = [i for i in range(1, 10)]
    if k == 1:
        return n
    if k >= 2:
        stack = numbers[0: k]
    while True:
        if sum(stack) == n :
            result.append(stack)
            for i in range(1, tag+1):
                pass


if __name__ == "__main__":
    # combinationSum(3, 9)
    s = Stack()
    s.push(1)

