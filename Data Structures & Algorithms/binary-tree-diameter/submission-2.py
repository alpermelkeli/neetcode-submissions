# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.traverse(0, root)

    def traverse(self, level, root):
        if not root: 
            return 0

        leftVal = self.traverse(level + 1, root.left)
        rightVal = self.traverse(level + 1, root.right)  
        if level == 0:
            return leftVal + rightVal
        if leftVal + rightVal > max(leftVal, rightVal) + level:
            return leftVal+rightVal
        else:
            return max(leftVal, rightVal) + 1 
        

        