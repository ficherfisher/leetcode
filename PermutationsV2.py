
def permuate(nums):
    result = []
    length = len(nums)
    def tracking(temp, NewNums):
        if len(temp) == length:
            if list(temp) not in result:
                result.append(list(temp))
            return
        for i in NewNums:
            temp.append(i)
            NewNums.remove(i)
            New = list(NewNums)
            tracking(temp, New)
            NewNums.insert(0, i)
            temp.pop()
    tracking([], nums)
    return result


if __name__ == "__main__":
    nums = [1, 1, 3]
    print(permuate(nums))


