# Time O(n)
# Space O(1)
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        # Loop over the list and use python's reverse syntax to check if a word equals it's reverse
        # If the word is found, return immediately 
        # If no word is found, return empty string

        for w in words:
            if w == w[::-1]:
                return w
        
        return ""