class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        
        for i, l in enumerate(s):
            if count[l] == 1:
                return i
        
        return -1
