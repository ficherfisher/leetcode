
def symbolMatch(string):
    hashtable = dict()
    hashtable[")"] = "("
    hashtable["}"] = "{"
    hashtable["]"] = "["
    stack = []
    for i in string:
        if i not in hashtable:
            stack.append(i)
        else:
            temp = stack.pop()
            if temp != hashtable[i]: return False
    if len(stack) == 0 :return True
    else: return False



if __name__ == "__main__":
    string = "{{[()]}}"
    print(symbolMatch(string))



