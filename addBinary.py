
def addBinary(a, b):
    n = min(len(a), len(b))
    m = max(len(a), len(b))
    i = n - 1
    j = m - 1
    carry = 0
    result = []
    if len(a) > len(b):
        temp = str(b)
        b = a
        a = temp
    while i >= 0:
        value = (int(a[i]) + int(b[j]) + carry) % 2
        carry = (int(a[i]) + int(b[j]) + carry) // 2
        result.insert(0, str(value))
        i -= 1
        j -= 1
    if len(a) < len(b): temp = b
    else: temp = a
    while j >= 0:
        value = (int(temp[j]) + carry) % 2
        carry = (int(temp[j]) + carry) // 2
        result.insert(0, str(value))
        j -= 1
    if carry == 1: result.insert(0, str(carry))
    return "".join(result)



if __name__ == "__main__":
    a = "1010"
    b = "1011"
    print(addBinary(a, b))


