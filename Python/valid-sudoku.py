class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_set = [set() for _ in range(9)]
        c_set = [set() for _ in range(9)]
        sq_set = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in r_set[r] or board[r][c] in c_set[c] or board[r][c] 
                    in sq_set[(r // 3) * 3 + (c // 3)]:
                    return False
                
                
                r_set[r].add(board[r][c])
                c_set[c].add(board[r][c])
                sq_set[(r // 3) * 3 + (c // 3)].add(board[r][c])
        
        return True
