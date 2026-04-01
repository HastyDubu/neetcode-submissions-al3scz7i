# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder and not inorder:
            return None
        
        n = preorder[0]
        mid = inorder.index(n)
        node = TreeNode(n)
        node.left = self.buildTree(preorder[1 :mid + 1], inorder[:mid])
        node.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return node