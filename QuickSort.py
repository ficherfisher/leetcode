def sortList(head, low, high):
    if low < high:
        pi = partition(head, low, high)
        sortList(head, low, pi-1)
        sortList(head, pi+1, high)


def partition(head, low, high):
    i = low - 1
    pivot = head[high]
    for j in range(low, high):
        if head[j] <= pivot:
            i += 1
            head[i], head[j] = head[j], head[i]
    head[i+1], head[high] = head[high], head[i+1]
    return i+1


if __name__ == "__main__":
    head = [6, -1, -2, 4, 1, 5, 3, 0]
    sortList(head, 0, len(head)-1)
    print(head)


