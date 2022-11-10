# Time O(n)
# Space O(n)
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string

class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        # Initiate a stack using deque since append and pop
        # actions run in constant time
        
        stack = deque()
        
        # Go through each letter in the string checking if the
        # last letter added to the stack is the same as the current
        # if so, we will keep removing from the stack until they are
        # not the same and continue.
        # If the letters aren't the same, add to stack and continue
        
        for l in s:
            if stack and l == stack[-1]:
                while stack and l == stack[-1]:
                    stack.pop()
            else:
                stack.append(l)
        
        return "".join(stack)
            
            
