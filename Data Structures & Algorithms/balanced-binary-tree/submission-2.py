# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
                return True
        left = self.height(root.left)
        right = self.height(root.right)
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
            if not root:
                return 0
            if root and not root.left and not root.right:
                return 1
            
            if root:
                left = self.height(root.left)
                right = self.height(root.right)
                return 1 + max(left, right)