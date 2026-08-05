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
        
        node = preorder[0]
        index = inorder.index(node)
        newNode = TreeNode(node)
        newNode.left = self.buildTree(preorder[1 :index + 1], inorder[:index])
        newNode.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return newNode