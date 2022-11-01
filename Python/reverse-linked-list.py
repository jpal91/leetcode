# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         node = head
#         prev = None
        
#         while node:
#             tmp = node.next
#             node.next = prev
#             prev = node
#             node = tmp
        
#         return prev
        
        def build(i, arr):
            if i < 0:
                return None
            
            return ListNode(arr[i], build(i - 1, arr))
        
        vals = []
        node = head
        
        while node:
            vals.append(node.val)
            node = node.next
        
        return build(len(vals) - 1, vals)
        
        
