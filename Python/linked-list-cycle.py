# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head.next
        fast = head.next.next
        
        while fast:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next if fast.next else None
        
        return False
