# Time: O(n log(n))
# Space: O(n)
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # Relatively straightforward solution. We need to try and 
        # make sure that the smallest number in the list is always the one
        # that is switched over to a negative to maximize our sum
        
        # To do this, we use a heapq which will always pop the smallest number in the list
        # Each time, changing it to it's negative and adding it back in. If the number was
        # relatively far away from 0, it will be added to the back of the heapq and all 
        # numbers in the heapq (while k > 0) will end up being in the back while smaller
        # values closer to 0 end up being in the front, minimizing any overall change when they are
        # multiplied by -1
        
        heapq.heapify(nums)
        
        while k > 0:
            next_num = heapq.heappop(nums)
            heapq.heappush(nums, next_num * - 1)
            k -= 1
        
        return sum(nums)
