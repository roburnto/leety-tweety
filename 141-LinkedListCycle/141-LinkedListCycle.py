# Last updated: 8/29/2025, 9:51:39 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast= fast.next.next
            slow = slow.next
            if slow == fast:
                return True

        
        return False