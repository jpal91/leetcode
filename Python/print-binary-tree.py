# Time: O(n)
# Space: O(n)
# https://leetcode.com/problems/print-binary-tree

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:        
        
        # First initiate DFS in order to find the max height of the tree
        
        def dfs(root, h):
            if root is None:
                return h
            
            # Returns the higher of the left or right branch
            
            return max(dfs(root.right, h + 1), dfs(root.left, h + 1))
        
        height = dfs(root, 0)
        
        # After use BFS in order to create new matrix based on the height

        def bfs(root):
            q = deque([root])
            board = []
            
            while q:
                
                n = len(q)
                arr = [''] * (2 ** height - 1)

                # In order to maintain each level of the tree, iterate a set number of times based on the prior
                # number of nodes added in the queue. For each level, create an empty array based on the height
                # and instructions from the problem

                for _ in range(n):
                    (r, c, node, lr) = q.popleft()
                    
                    # Base case for first go around. Number will always be placed exactly in the middle of row list
                    if not lr:
                        n_c = len(arr) // 2
                        arr[n_c] = str(node.val)
                    
                    # If the prior node added to the queue was tagged as 'l' (left node) or 'r' (right node), calculate the 
                    # new position based on the prior node and problem definitions
                    elif lr == 'l':
                        n_c = c - (2 ** (height - r - 1))
                        arr[n_c] = str(node.val)
                    elif lr == 'r':
                        n_c = c + (2 ** (height - r - 1))
                        arr[n_c] = str(node.val)
                    
                    # To avoid adding None nodes, check for each left and right and include the positioning of current node
                    # so it's new position can be calculated relative to the current node's position
                    if node.left:
                        q.append((r + 1, n_c, node.left, 'l'))
                    if node.right:
                        q.append((r + 1, n_c, node.right, 'r'))
                
                # At each level, the row is added to the main board
                board.append(arr)
            
            return board
        
        # Return bfs function with base case and first node
        return bfs((0, 0, root, None))