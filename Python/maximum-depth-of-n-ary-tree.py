# Time: O(n)
# Space: O(n)
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # Base case if no root
        if root is None:
            return 0
        
        q = deque([root])
        max_height = 0
        
        # Queue up initial node and BFS each level to find height

        while q:
            n = len(q)
            
            # Levels of the queue have multiple children
            # to get an accurate count, iterate over the number of the children in that level
            # adding each subsequent child to the queue creating next level
            # Each level is an additional height of 1

            for _ in range(n):
                node = q.popleft()
                
                for child in node.children:
                    if not child:
                        continue
                    else:
                        q.append(child)

            max_height += 1
        
        return max_height