# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def leaf(node):
            if not node: return []
            return leaf(node.left)+leaf(node.right) or [node.val]
        
        return leaf(root1)==leaf(root2)
            
                
        