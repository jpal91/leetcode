# Time: O(n)
# Space: O(n)
# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # Handles edge cases for 1 and 2
        # If there's only 1 row, answer will == string
        # If there's two, the answer is a concantenation of every other word starting from 0 then 1
        if numRows == 1:
            return s
        elif numRows == 2:
            return s[::2] + s[1::2]
        
        # Initialize an empty array with sub empty arrays for rows
        # The length equals the numRows
        
        n = len(s)
        res = [[] for x in range(numRows)]

        # i = index of string, # r = row of res, # d = direction (up or down)
        i, r, d = 0, 0, -1

        # Each iteration will append one letter to a row in res, continue until no more letters
        # ie r = 1 -> The row of res at index 1 will be appended

        while i < n:
            # If we're at the top row or bottom row, we will zig-zag and reverse course
            # d will either be -1 or 1 depending on if we're moving up or down
            # If we're on the bottom row we take off 2 as the next letter will actually be on the second to last index

            if r == 0 or r == numRows:
                d *= -1
                if r == numRows:
                    r += d * 2
            
            res[r].append(s[i])
            i += 1
            r += d

        # At the end we should have a list of lists that will be combined together in order
        # Ex: s = 'ABCDEFGHI' numRows = 3
        # res = [
        #     ['A',     'E',    'I'],
        #     ['B', 'D' 'F' 'H'],
        #     ['C'      'G'],
        # ]
        # (spacing for visualization)
        # Each list will be joined and the aggregate of the lists will be joined into one string

        return "".join(["".join(y) for y in res])