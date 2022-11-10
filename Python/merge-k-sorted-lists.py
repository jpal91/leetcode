# Time: O(n log(n))
# Space: O(n)
# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        res = []
        
        # Iterating through the list of ListNodes we will add each value
        # using bisect so that we can maintain the order overall we will
        # loop this until all lists have been depleted, deleting empty nodes
        # as we go
        
        while lists:
            for i,l in enumerate(lists):
                if l is None:
                    del lists[i]
                    continue
                bisect.insort_left(res, l.val)
                lists[i] = l.next
        
        n = len(res)
        
        if not res:
            return None
        
        node = ListNode()
        head = node
        
        # Finally using the new list which contains all values in order, we
        # simply build a new ListNode with each value in the list
        
        for i in range(n):
            node.val = res[i]
            if i == n - 1:
                break
            node.next = ListNode()
            node = node.next
            
        
        return head
                
            
            
