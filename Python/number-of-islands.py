# Time: O(n)
# Space: O(1)
# https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(root):
            # Create a queue for bfs and pop values until 
            # no other nodes fit the criteria to be added and
            # the loop ends
            q = deque([root])
            
            while q:
                row, col = q.popleft()
                
                grid[row][col] = '0'
                
                # Checks each direction around our current node (top, down, left, right)
                # and determines if the root is valid (actually on the grid) and if it's already
                # a "0" value in which case we would want to skip it as we are only interested in
                # adjacent "1" cells from our original root cell 
                #
                # As we check adjacent cells, we also change their value to '0' so they won't be added
                # again to the queue later on when we're checking adjacent cells
                
                for y, x in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    r, c = row + y, col + x
                    
                    if r < 0 or r >= n_r or c < 0 or c >= n_c:
                        continue
                    elif grid[r][c] == '0':
                        continue
                    grid[r][c] = '0'
                    q.append((r, c))
        
        islands = 0
        n_r, n_c = len(grid), len(grid[0])
        
        # Iterates through the grid to find the first '1' value and send
        # to the bfs helper function. After the first round, many '1' values should
        # become '0'. This change benefits us as we can skip over these values knowing
        # the cells have already been checked
        # Finally we increment the island count by 1 as the bfs function would have changed 
        # any valid adjacent cells to '0', essentially deleting the island from the grid
        
        for r in range(n_r):
            for c in range(n_c):
                if grid[r][c] == '0':
                    continue
                bfs((r, c))
                islands += 1
        
        return islands

