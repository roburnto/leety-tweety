# Last updated: 8/29/2025, 9:38:38 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1 or not list2:
            return list1 if not list2 else list2
        curr1 = list1
        curr2 = list2
        dummy = head =None
        if curr1.val < curr2.val:
            dummy = curr1
            curr1 = curr1.next
        else:
            dummy = curr2
            curr2 = curr2.next
        head = dummy
        while curr1 and curr2:
            if curr1.val < curr2.val:
                dummy.next = curr1
                curr1 = curr1.next
            else:
                dummy.next = curr2
                curr2 = curr2.next
            dummy = dummy.next
        if curr1:
            dummy.next = curr1
        elif curr2:
            dummy.next = curr2
        
        return head



                



