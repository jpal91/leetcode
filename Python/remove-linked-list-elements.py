# Time: O(n)
# Space: O(1)
# https://leetcode.com/problems/remove-linked-list-elements

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Track the current node and the node right before the current
        node = head
        prev = None
        
        # If the node's value equals the target either -
        # If there is not previous node, this means we're at the head, move the head forward
        # IF there is a previous, change the previous nodes next to the one after, essentially skipping the current node
        while node:
            if node.val == val:
                if not prev:
                    head = head.next
                    node = head
                    continue
                else:
                    prev.next = node.next
                    node = node.next
                    continue
                    
            prev = node
            node = node.next
        return head