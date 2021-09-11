
def convert(s, numRows):
    if numRows == 1: return s
    result = [[] for i in range(numRows)]
    location = 0
    count = 0
    for index, i in enumerate(s):
        result[count].append(i)
        if location == 0:
            count = count + 1
        if location == 1:
            count = count - 1
        if count == numRows - 1:
            location = 1
        if count == 0:
            location = 0
    str = ""
    for i in result:
        for j in i:
            str = str + j
    return str


if __name__ == "__main__":
    strings = "ABsad"
    numRows = 2
    print(convert(strings, numRows))



