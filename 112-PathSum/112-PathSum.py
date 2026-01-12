# Last updated: 1/12/2026, 1:42:09 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def backtrack(root, sum):
            if not root:
                return False

            sum -= root.val
            if not root.left and not root.right:
                return sum == 0
            
            return backtrack(root.left, sum) or backtrack(root.right,sum)

        
        return backtrack(root, targetSum)