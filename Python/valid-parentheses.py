# Time: O(n)
# Space: O(n)
# https://leetcode.com/problems/valid-parentheses/submissions/

class Solution:
    def isValid(self, s: str) -> bool:
        # Create a stack to store open brackets
        q = deque()
        
        # Closed brackets are mapped out to their open pairs
        p_map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        # As we go through the string, only open brackets will be added to the queue
        # Once we reach a close bracket, we check if the last open bracket added is the same type as this close bracket
        # If it is, pop the list and move to the next, if not we know it's invalid and immediately return False
        for p in s:
            if p not in p_map:
                q.append(p)
            elif not q or q[-1] != p_map[p]:
                return False
            else:
                q.pop()
        
        # If there are still items in the stack/queue at the end, that means not every open bracket was closed 
        # and therefore we should return False
        return not q