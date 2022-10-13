# Time: O(n)
# Space: O(n)
# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Initiate set to track each number visited in array
        unique_vals = set()
        
        for num in nums:

            # If the number was already added to the set, it's a duplicate, return True
            # Else, add number into set to compare against future numbers in array

            if num in unique_vals:
                return True
            else:
                unique_vals.add(num)
        
        # If no number returned True, there must be no duplicates

        return False