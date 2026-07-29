# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            total_count = 0
            return total_count
        if root and not root.left and not root.right:
            total_count = 1
            return total_count
        
        if root.left or root.right:
            left_count = self.maxDepth(root.left)
            right_count = self.maxDepth(root.right)
            total_count = 1 + max(left_count, right_count)
        
        return total_count