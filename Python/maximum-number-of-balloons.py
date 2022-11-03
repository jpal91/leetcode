# Time: O(n)
# Space: O(n)
# https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Initialize the target (balloon) and a counter that will count up all letters
        # within the text that are also letters of balloon
        b = 'balloon'
        count = Counter([t for t in text if t in b])
        n, i, poss = len(b), 0, 0
        
        # Loop over 'balloon', each time taking out 1 target letter from the counter
        # If there are no more letters at the index i, we can't finish the word balloon, so immediately break
        # Once i reaches the end of 'balloon', we know that we've spelled it out at least one more time so increment poss variable by 1
        while count:
            if count[b[i]] == 0:
                break
            else:
                count[b[i]] -= 1
                i += 1
            
            if i == n:
                i = 0
                poss += 1
                
        return poss
