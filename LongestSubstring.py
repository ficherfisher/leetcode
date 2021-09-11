
def lengOflengthestSubstring(Strings):
    tags = [Strings[0]]
    maxes = 0
    for i in Strings[1:]:
        if i not in tags:
            tags.append(i)
        else:
            if len(tags) > maxes:
                maxes = len(tags)
            index = tags.index(i)
            del tags[0: index+1]
            tags.append(i)
        print(tags)
    return maxes


if __name__ == "__main__":
    print(lengOflengthestSubstring("abcabcbb"))




