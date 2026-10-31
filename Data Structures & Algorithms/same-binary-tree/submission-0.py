# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a = [] 
        self.preOrder(p, a)
        b = []
        self.preOrder(q, b)
        return a == b

    def preOrder(self, root, l):
        if not root:
            l.append(None)
            return

        l.append(root.val)
        self.preOrder(root.left, l)
        self.preOrder(root.right, l)
