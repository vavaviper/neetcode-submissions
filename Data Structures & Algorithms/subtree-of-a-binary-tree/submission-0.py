class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(root, subRoot):
            if not root and not subRoot:
                return True

            if not root or not subRoot:
                return False

            if root.val != subRoot.val:
                return False

            return isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)

        def traverse(root):
            if not root:
                return False

            if isSame(root, subRoot):
                return True

            return traverse(root.left) or traverse(root.right)

        return traverse(root)