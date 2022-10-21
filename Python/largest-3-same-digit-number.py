# Time: O(n)
# Space: O(1)
# https://leetcode.com/problems/largest-3-same-digit-number-in-string

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num, max_s = '-1', ''
        n = len(num)

        # Iterate over string, if the last three string digits are equal, append to max_s and set the current value as the new max
        # After the first number is found, any number less will be skipped over 
        
        for i in range(2, n):
            if num[i] == num[i - 1] == num[i - 2] and num[i] > max_num:
                max_s = num[i] * 3
                max_num = num[i]
        return max_s