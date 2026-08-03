# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        visited = deque()
        visited.append(root)

        output = [[]]
        depth = 0
        num = 1

        while visited:
            curr = visited.popleft()

            if curr.left:
                visited.append(curr.left)

            if curr.right:
                visited.append(curr.right)

            output[depth].append(curr.val)

            num -= 1

            if num == 0:
                depth += 1
                num = len(visited)

                if visited:
                    output.append([])

        return output