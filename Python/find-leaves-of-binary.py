# Time: O(n)
# Space: O(n)
# https://leetcode.com/problems/find-leaves-of-binary-tree/

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Create a separate DFS function which will go to the leaf nodes
        # appending the value to an array, then delete the node
        def dfs(root):
            if not root:
                return None
            if not root.left and not root.right:
                arr.append(root.val)
                root = None
                return None
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            
            return root
        
        res = []
        # Loop until the root is None each time updating the TreeNode by removing
        # it's leaves. Each loop a new blank array is created to add to the res object

        while root:
            arr = []
            root = dfs(root)
            res.append(arr)
        
        return res

