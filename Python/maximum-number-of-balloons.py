# Time: O(n)
# Space: O(n)
# https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = 'balloon'
        # Create a Counter which will loop over the text once and only take letters in 'balloon'
        count = Counter([t for t in text if t in b])
        n, i, poss = len(b), 0, 0
        
        # Loops over the 'balloon' string and decrements the letter at the index i
        while count:
            # If we get to a letter and the count is 0, we know we cannot finish the word, so break
            if count[b[i]] == 0:
                break
            else:
                # If there are still letters available for the letter at this index i, decrease it by 1 and
                # move to the next letter
                count[b[i]] -= 1
                i += 1
            
            # Once we've reached the end of the string, we know we're able to spell balloon at least one more time
            # Increase the possible maximum possible by 1 and start over at the beginning

            if i == n:
                i = 0
                poss += 1
                
        return poss