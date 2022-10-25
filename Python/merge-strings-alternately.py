# Time: O(n)
# Space: O(n)
# https://leetcode.com/problems/merge-strings-alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        n1, n2 = len(word1), len(word2)
        res = ''

        # Very simple for loop
        # The max length of either string is determined and the for loop will stop once it reaches the max of both
        # Alternates between both strings by just adding word1[i] first and word2[i] second
        # Once it reaches the end of one string (if they are not the same length), it finishes up on the longer string

        n = max(n1, n2)

        for i in range(n):
            if i < n1 and i < n2:
                res += word1[i]
                res += word2[i]
            elif i >= n1:
                res += word2[i]
            elif i >= n2:
                res += word1[i]
        
        return res