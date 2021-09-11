
def countAndSay(n):
    result = ["1", "11", "21", "1211", "111221"]
    begin = "111221"
    if n <= 5:
        return result[n - 1]
    for i in range(n - 5):
        begin = counts(begin)
    return begin

def counts(begin):
    res = ""
    cnt = 1
    ch = begin[0]
    for i in begin[1:]:
        if ch == i:
            cnt += 1
        else:
            res += str(cnt)
            res += ch
            cnt = 1
            ch = i
    res += str(cnt)
    res += ch
    return res


if __name__ == "__main__":
    n = 1
    print(countAndSay(n))

