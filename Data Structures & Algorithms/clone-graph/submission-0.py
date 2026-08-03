"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        if not node:
            return None

        def search(node):
            # Already cloned
            if node in clones:
                return clones[node]

            # Create clone
            clones[node] = Node(node.val)

            # Clone all neighbors
            for neighbor in node.neighbors:
                clones[node].neighbors.append(search(neighbor))

            return clones[node]

        return search(node)