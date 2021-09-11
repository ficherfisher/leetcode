# print(sorted(Strings[0]))
# 可以使用sorted函数对小写字母排序

def groupAnagrams(strings):
    result = []
    index = -1
    hashtable = dict()
    for i in strings:
        temp = str(sorted(i))
        if temp not in hashtable:
            index += 1
            result.append([])
            hashtable[temp] = index
            result[index].append(i)
        else:
            a = hashtable[temp]
            result[a].append(i)
    return result


if __name__ == "__main__":
    Strings = ["a"]
    print(groupAnagrams(Strings))

