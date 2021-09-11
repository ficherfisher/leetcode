# two Point

def maxArea(height):
    result = 0
    length = len(height) - 1
    i = 0
    j = length
    while True:
        if i >= j: break
        temp = (j - i) * min(height[i], height[j])
        if temp > result:
            result = temp
        if height[i] > height[j]:
            j = j - 1
        else:
            i = i + 1
    return result


if __name__ == "__main__":
    height = [4,3,2,1,4]
    print(maxArea(height))







