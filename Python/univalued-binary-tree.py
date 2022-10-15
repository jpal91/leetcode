# Time: O(n) on average with best case of O(1)
# Space: O(n)
# https://leetcode.com/problems/univalued-binary-tree/

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # Set a variable equal to the first root's value
        # If any do not match this, the tree cannot be uni-value
        number = root.val

        q = deque([root])
        
        # BFS through each level
        # If a root's value does not match the number variable, immediately return False
        # Else add valid right and left nodes to the queue and continue
        # If all node values match the initial number, return True

        while q:
            n = len(q)
            
            for _ in range(n):
                node = q.popleft()
                
                if node.val != number:
                    return False
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return True