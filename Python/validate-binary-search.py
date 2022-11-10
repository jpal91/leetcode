# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n)
# Space: O(1)
# https://leetcode.com/problems/validate-binary-search-tree/

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function for dfs
        # Goes to each node and determines whether or not the value is
        # less than the minimum value for that branch or greater than the max   
        
        def dfs(root, min_v, max_v):
            if root is None:
                return True
            elif root.val <= min_v or root.val >= max_v:
                return False
            
            # Each time a left or right branch is searched, the value gets updated
            # based on whether it's going to the left branch (values should be less than)
            # or right branch (values should be greater)
            
            return dfs(root.left, min_v, root.val) and dfs(root.right, root.val, 
                max_v)
        
        # If both the left and right branches reach their leaves without returning False,
        # the tree is valid
        
        return dfs(root, float('-inf'), float('inf'))
