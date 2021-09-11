
def PlusOne(digits):
    carry = 0
    result = []
    temp = 1
    for i in reversed(digits):
        value = (i + carry + temp) % 10
        carry = (i + carry + temp) // 10
        result.insert(0, value)
        temp = 0
    if carry == 1: result.insert(0, carry)
    return result


if __name__ == "__main__":
    digits = [9, 0, 9]
    print(PlusOne(digits))


