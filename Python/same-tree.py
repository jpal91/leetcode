# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n)
# Space: O(1)
# https://leetcode.com/problems/same-tree

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Helper function to traverse both trees simultaneously
        # Will check at each level whether or not the roots are equivalent in value
        # As it goes to the next level, both trees will be sent to the recursive call
        # with the same branch to make sure we're comparing the same node
        
        def dfs(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif root1 is None or root2 is None:
                return False
            elif root1.val != root2.val:
                return False
            
            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
        
        return dfs(p, q)
