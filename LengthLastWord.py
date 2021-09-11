
def lengOfLastWord(str):
    LastWord = str.split(" ")
    temp = []
    for i in LastWord:
        if len(i) > 0:
            temp.append(len(i))
    return int(temp[-1])


if __name__ == "__main__":
    strings = "hello world "
    print(lengOfLastWord(strings))



