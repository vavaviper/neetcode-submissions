class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def maxHeight(node):
            if not node:
                return 0

            left = maxHeight(node.left)
            right = maxHeight(node.right)

            # diameter passing through this node
            self.diameter = max(self.diameter, left + right)

            # return height only
            return 1 + max(left, right)

        maxHeight(root)
        return self.diameter