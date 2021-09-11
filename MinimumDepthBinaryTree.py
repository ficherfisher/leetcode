class TreeNode:
    def __init__(self, val=-1001, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        head = self.createBinaryTree(root, 0)
        a = 1

    def createBinaryTree(self, array, index):
        treeNode = TreeNode()
        if index < len(array):
            treeNode = TreeNode(array[index])
            treeNode.left = self.createBinaryTree(array, 2*index+1)
            treeNode.right = self.createBinaryTree(array, 2*index+2)
        return treeNode


if __name__ == "__main__":
    root = [2,-1001,3,-1001,4,-1001,5,-1001,6]
    solution = Solution()
    solution.minDepth(root)

