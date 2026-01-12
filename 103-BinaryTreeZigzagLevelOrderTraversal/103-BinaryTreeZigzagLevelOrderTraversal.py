# Last updated: 1/12/2026, 1:42:10 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        q = collections.deque()
        q.append(root)
        counter = 0
        
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                if counter % 2 == 1:
                    res.append(level[::-1])
                else:
                    res.append(level)
            counter +=1
            
        return res