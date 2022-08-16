"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        def height(root):
            if len(root.children)==0: return 1
            return 1+max([height(i) for i in root.children])
        return height(root)
        