class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def rotateRight(head, k):
    length_chain = 0
    point = head
    while point.next != None:
        length_chain += 1
        point = point.next
    if k % length_chain == 0: return head.next
    else: temp = length_chain - k % length_chain
    point.next = head.next
    newPoint = head
    while temp > 0:
        newPoint = newPoint.next
        temp -= 1
    a = newPoint.next
    newPoint.next = None
    return a


if __name__ == "__main__":
    head = [0, 1, 2, 3, 4, 5, 6]
    k = 18
    root = ListNode(-101)
    temp = root
    for i in head:
        temp.next = ListNode(i)
        temp = temp.next
    newHead = rotateRight(root, k)
    while newHead != None:
        print(newHead.val, end=" ")
        newHead = newHead.next


