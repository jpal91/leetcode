# Time: O(n ** 2)
# Space: O(n)
# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        # Array must be sorted for this method as the two pointers 
        # will increment or decrement based on sum being over or under 0
        # Also this is used to avoid duplicates
        nums.sort()

        for i, num in enumerate(nums):
            # Checks if the last number is the same as the current
            # Continues to avoid duplicates
            if i > 0 and num == nums[i - 1]:
                continue
            
            l, r = i + 1, n - 1
            
            # For each number, two pointers will be defined
            # One directly in front of the current number(l), and the last number in the index (r)
            # The sum is taken and since the list is sorted, if the number is greater than 0, the right pointer moves down
            # else the left pointer moves up

            while l < r:
                n_list = [num, nums[l], nums[r]]
                sum_nums = sum(n_list)
                
                if sum_nums == 0:
                    res.append(n_list)
                    l += 1
                    r -= 1
                    
                    # To avoid duplicates, the right pointer keeps moving if the last num[r] is the same as the current

                    while r > 1 and nums[r] == nums[r + 1]:
                        r -= 1
                elif sum_nums > 0:
                    r -= 1
                else:
                    l += 1
            
            # Once the number on the current index is 0, any numbers larger cannot sum to 0 as the list is sorted
            # If at 0 and there are other 0s in the list, it will have already been appended once, so no need to go over again

            if i > 0 and num >= 0:
                break
        
        return res