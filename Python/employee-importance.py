"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

# Time: O(n)
# Space: O(n)
# https://leetcode.com/problems/employee-importance

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        # Initialize a hash map and map each employee with their importance and 
        # subordinates by id
        
        imp_map = defaultdict(tuple)
        
        for e in employees:
            imp_map[e.id] = (e.importance, e.subordinates)
        
        # Ex. imp_map[1] == (5, [2, 3])
        
        q = deque([imp_map[id]])
        score = 0
        
        # Starting with the target employee, add their importance and subsequently 
        # each
        # of their subordinates importance as you add them into the queue
        # Will traverse each level until there are no more subordinates and returns 
        # score
        
        while q:
            n = len(q)
            
            for _ in range(n):
                rate, subs = q.popleft()

                score += rate
                
                for s_id in subs:
                    q.append(imp_map[s_id])
        
        return score
            
            
