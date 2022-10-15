# Time: O(n + n) -> O(n)
# Space: O(n)
# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a hash table to track each course and it's required prerequisites
        c_list = defaultdict(list)
        
        # Add each course and append the prerequisite to a list
        for c, p in prerequisites:
            c_list[c].append(p)
        
        def dfs(c, vis, memo):
            if c in memo:
                return memo[c]
            if c in vis:
                return False
            if c not in c_list:
                return True

            # Add the course to a set to track if we're looping
            # For each of the courses within the course's prereq list, dfs to determine if it loops back to the original c
            # If it does, return False, else remove the course that didn't loop from visited and return True


            vis.add(c)
            for node in c_list[c]:
                if not dfs(node, vis, memo):
                    return False
            vis.remove(c)
            
            return True
        
        # Loop through every course, if it causes a loop, immediately return False
        # If it doesn't, memoize it as True so if it's visited within DFS, the function stops and no additional processing is needed
        # If all courses do not cause a loop, return True

        memo = {}
        for i in range(numCourses):

            if not dfs(i, set(), memo):
                return False
            memo[i] = True

        return True