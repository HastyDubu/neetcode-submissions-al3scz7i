"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}

        def dfs(node):
            if node in clone:
                return clone[node]
            
            newNode = Node(node.val)
            clone[node] = newNode
            for nei in node.neighbors:
                clone[node].neighbors.append(dfs(nei))
            return newNode
        
        
        return dfs(node) if node else None