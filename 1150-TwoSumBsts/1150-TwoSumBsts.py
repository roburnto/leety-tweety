# Last updated: 1/12/2026, 1:41:30 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        def inorder_traversal(node,values):
            if node == None:
                return
            
            inorder_traversal(node.left, values)
            values.add(node.val)
            inorder_traversal(node.right,values)
            
        def check_complements(node, values):
            if node == None:
                return False
            if target - node.val in values:
                return True
            return check_complements(node.left, values) or check_complements(node.right, values)
        
        set1 = set()
        
        inorder_traversal(root1, set1)
        
        return check_complements(root2, set1)