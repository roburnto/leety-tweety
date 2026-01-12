# Last updated: 1/12/2026, 1:41:39 PM
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        
        stack = [root]

        while stack:
            n = stack.pop()
            res.append(n.val)
            for i in range(len(n.children)-1,-1,-1):
                stack.append(n.children[i])
        
        return res
            