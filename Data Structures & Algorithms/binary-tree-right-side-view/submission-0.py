# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #returning this as a list
        output = []
        #queue for what to traverse next
        q = deque([root])

        #while q exists
        while q:
            #variable for the most right one
            rightSide = None
            qLen = len(q)

            #go through current q
            #use for i in range so it only goes through the current level
            for i in range(qLen):
                #remove first val in queue
                node = q.popleft()
                if node:
                    #assign that value as the right side variable
                    rightSide = node
                    #append the next level to the queue
                    q.append(node.left)
                    q.append(node.right)
            #add that right side variable to the output
            if rightSide:
                output.append(rightSide.val)
        return output                
       