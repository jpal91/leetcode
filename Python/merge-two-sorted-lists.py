# Time: O(n)
# Space: O(n)
# https://leetcode.com/problems/merge-two-sorted-lists

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Checks edge cases and returns immediately
        # If both list1 and list2 are None, return None
        # If one list is not None, return the list that has a value
        if not list1 and not list2:
            return None
        elif not list1 or not list2:
            return list1 or list2
        
        # Create an empty ListNode instance to start the new list from
        # Since the head will be returned, a pointer variable will be used to traverse
        # Finally two variables to traverse the individual lists are added
        head = ListNode()
        ptr = head
        l1, l2 = list1, list2
        
        # Each list node is compared to see the smaller value and this is added to the 
        # pointer node as a new ListNode
        # Whichever value is added, that list is progressed forward
        # Finally if there's still values left, a new ListNode is added to the end for the next value and the pointer is moved forward
        while l1 or l2:
            if not l1 and l2:
                ptr.val = l2.val
                l2 = l2.next
                
            elif l1 and not l2:
                ptr.val = l1.val
                l1 = l1.next
            
            elif l1.val < l2.val:
                ptr.val = l1.val
                l1 = l1.next
            
            else:
                ptr.val = l2.val
                l2 = l2.next
            
            if l1 or l2:
                ptr.next = ListNode()
                ptr = ptr.next
        
        return head