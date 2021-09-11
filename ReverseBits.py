
def reverseBits(num):
    if num == 0: return 1
    num_bin = list(bin(num).replace("0b", ""))
    print(num_bin)
    table = []
    tag = num_bin[0]
    count = 1
    for i in range(len(num_bin) - 1):
        if tag == num_bin[i + 1]:
            count = count + 1
        else:
            temp = {}
            temp[tag] = count
            count = 1
            tag = num_bin[i + 1]
            table.append(temp)
    temp = {}
    temp[tag] = count
    table.append(temp)
    maxes1 = 0
    for i in range(len(table) - 2):
        _1 = table[i]
        _2 = table[i+1]
        _3 = table[i+2]
        if list(_1.keys())[0] == "1" and list(_2.keys())[0] == "0" and list(_3.keys())[0] == "1" and list(_2.values())[0] == 1:
            new_max = list(_1.values())[0] + list(_3.values())[0] + 1
            if new_max > maxes1:
                maxes1 = new_max
    maxes2 = 0
    for i in range(len(table)):
        _1 = table[i]
        if list(_1.keys())[0] == "1":
            new_max = list(_1.values())[0] + 1
            if new_max > maxes2:
                maxes2 = new_max
    return max(maxes1, maxes2)


if __name__ == "__main__":
    print(reverseBits(546321879))

