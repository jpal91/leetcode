# Time: O(n log(n))
# Space: O(n)
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Sort the numbers and initalize an empty dict to be used as a hash map
        sort_dict = {}
        s_nums = sorted(nums)
        n = len(nums)
        
        # Fill the dict with the number as the key and it's corresponding index as the value
        # Will not override a previous key (duplicate number in array) so we can always get an
        # accurate answer as to how many numbers are larger in the array
        for i, num in enumerate(s_nums):
            if num not in sort_dict:
                sort_dict[num] = i
        
        # Change the number in the original array to it's sorted index
        for i in range(n):
            s_idx = sort_dict[nums[i]]
            nums[i] = s_idx
        
        return nums