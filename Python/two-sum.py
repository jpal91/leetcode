# Time: O(n)
# Space: O(n)
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initiate a hash table to track a nums difference from target and index
        hash_table = {}
        
        # Loop through nums array
        for i, num in enumerate(nums):
            # If the target appears in hash_table, return hash_table value (index) and current index
            if num in hash_table:
                return [hash_table[num], i]
            
            # If not found, store value in hash_table as the difference between number and target (key) and the index (value)
            
            target_diff = target - num
            hash_table[target_diff] = i