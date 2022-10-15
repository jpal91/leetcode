# Time: O(n ** 2) with O(n) being average
# Space: O(1)
# https://leetcode.com/problems/recover-binary-search-tree/
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        # DFS through the binary tree with min and max values for each root
        # If the root's val is greater than the max on a left tree, swap the values
        # Opposite on the right side of the tree
        # After one interation, it will be either a valid BST or still have values needing swapped

        def dfs(root, max_l, min_r):
            if root is None:
                return None
            
            # Checks if the value is valid, if not, swaps the values
            # The valid variable is updated to False in either case so we loop again until complete
            
            if root.val > max_l.val:
                self.valid = False
                max_l.val, root.val = root.val, max_l.val
            if root.val < min_r.val:
                self.valid = False
                min_r.val, root.val = root.val, min_r.val
            
            # The max of the left and right sides become the current value to make it a valid BST

            root.left = dfs(root.left, root, min_r)
            root.right = dfs(root.right, max_l, root)
            
            return root
        
        self.valid = False
        
        # Every loop will change the value to a presumption of True and run DFS
        # If values are swapped within DFS, the tree is invalid and we must loop again
        # The dfs function must be called once more after to confirm validity so best case complexity is O(n + n)

        while not self.valid:
            self.valid = True
            
            # Dummy ListNodes are added in to start, they are updated in the recursion 
            # Using ListNodes as variables allow for referencing back to a farther away node and swapping the value
            
            root = dfs(root, ListNode(float('inf'), None), ListNode(float('-inf'), None))
        
        return root