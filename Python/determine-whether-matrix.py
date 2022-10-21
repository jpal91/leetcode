# Time O(n)
# Space O(n)
# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        
        n_r, n_c = len(mat), len(mat[0])
        
        # First create an empty array to handle the first rotated possibility
        ro_90 = [[0 for x in range(n_c)] for y in range(n_r)]

        # In an attempt to try and stop the function from running through every possibility to get to False
        # I attempted to find some edge cases early on with two counters
        # Although it increases memory requirements, it greatly increases efficiency 
        count_mat = Counter()
        count_targ = Counter()
        
        # Go through the given matrix and place the first 90 degree rotated values
        # This is determined by first swapping the row and column, the new row will be the old column
        # The new column is the absolute difference between the old row and the last row
        # This also has a dual purpose of using our counters to determine if we have an equal number of 0s and 1s
        for r in range(n_r):
            for c in range(n_c):
                new_r = c
                new_c = abs(r - (n_r - 1))
                
                ro_90[new_r][new_c] = mat[r][c]
                count_mat[mat[r][c]] += 1
                count_targ[target[r][c]] += 1
        
        # First edge case checked and no more processing occurs if we determine the matrices do not have equal
        # counts of 0s and 1s
        if count_mat != count_targ:
            return False
        
        # Right after each rotation, the new rotation is checked to see if it fits so we can stop and return
        if ro_90 == target:
            return True
        
        # Rotated 180 degrees is just all rows and columns reversed
        ro_180 = [x[::-1] for x in mat][::-1]
        
        if ro_180 == target:
            return True
        
        ro_270 = [y[::-1] for y in ro_90][::-1]
        
        if ro_270 == target:
            return True
        
        return False