# Last updated: 1/12/2026, 1:41:43 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isIdentical(tree1, tree2):
            
            if not tree1 and not tree2:
                return True
            
            if not tree1 or not tree2:
                return False
            
            return (tree1.val == tree2.val and isIdentical(tree1.left, tree2.left) and isIdentical(tree1.right, tree2.right))
        
        def dfs(node):
            
            if not node:
                return False
            
            if node.val == subRoot.val and isIdentical(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        if not subRoot:
            return True
        if not root:
            return False
        
        return dfs(root)