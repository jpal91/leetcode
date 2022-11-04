# Time: O(n) for init, O(1) for sumRegion
# Space: O(n)
# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        Creates a prefix sum matrix from the original matrix
        Each row is added to the last cell, same for col
        """
        self.matrix = matrix
        self.n_r, self.n_c = len(matrix), len(matrix[0])
        
        for r in range(self.n_r):
            for c in range(1, self.n_c):
                self.matrix[r][c] += self.matrix[r][c - 1]
        
        for c in range(self.n_c):
            for r in range(1, self.n_r):
                self.matrix[r][c] += self.matrix[r - 1][c]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Calculates a region based on prefix sum
        
        The bottom right cell given is the sum of the region but it includes
        all rows and cells back to (0, 0). Because of this, we need to subtract
        the sum coming from the cell to the bottom and left of the region and
        the cell on the right and on top of the region to offset all other
        numbers provided from the prefix.
        
        Also if we end up having an offset of a row and column, we must add back in
        The cell (row - 1, col - 1) from the top left most square provided as well
        """
        offset_c = self.matrix[row2][col1 - 1] if col1 - 1 >= 0 else 0
        offset_r = self.matrix[row1 - 1][col2] if row1 - 1 >= 0 else 0
        add_org = self.matrix[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0
        
        return self.matrix[row2][col2] - offset_c - offset_r + add_org
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
