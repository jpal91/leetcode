# Time: O(n log(n))
# Space: O(1)
# https://leetcode.com/problems/meeting-rooms/

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort so that we know the next meeting we check will always have a start
        # time after the one we're checking
        intervals.sort()
        n = len(intervals)
        
        # Simply determining whether the start time of the current meeting starts before
        # the end time of the last
        # Since we know the start times are always ascending, we just need to know that 
        # the next meeting starts after the last meeting ends
        
        for i in range(1, n):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
            
        return True