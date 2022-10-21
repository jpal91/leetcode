# Time: O(n)
# Space: O(n)
# https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Initiate a dict to track each numbers index
        hash_m = {}
        
        # As we iterate through the list, each number will be added to the dict to track it's index
        # If we come to a duplicate, we determine if the absolute difference of the duplicates index and the current index is <= k -> return True
        # Else continue iterating while adding new number, index pairs

        for i, n in enumerate(nums):
            if n in hash_m and abs(hash_m[n] - i) <= k:
                return True
            else:
                hash_m[n] = i
        
        return False