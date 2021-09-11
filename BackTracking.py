# 一个数组的全排列


def backTracking(nums):
    result = []
    def track(temp, choice):
        if len(temp) == len(choice):
            result.append(list(temp))
            return
        for i in choice:
            if i in temp: continue
            temp.append(i)
            track(temp, choice)
            temp.pop()
    track([], nums)
    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(backTracking(nums))








