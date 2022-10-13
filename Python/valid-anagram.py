from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Initiate two counters, one for s and one for t
        # Counter will check how many of each letter we have within the given string
        
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Return if the first Counter == the second Counter
        # If the two strings have the same letters in the same quantities -> return True
        
        return count_s == count_t