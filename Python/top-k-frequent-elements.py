# Time: O(n log(n)) as Counter.most_common() must sort the list
# Space: O(n)
# https://leetcode.com/problems/top-k-frequent-elements

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Initialize counter which returns each elements frequency
        
        count_nums = Counter(nums)
        
        # Use Counter method most_common taking k as the argument
        # Returns list of top k elements by decreasing frequency in tuple pairs (element, frequency)
        # Iterate over list to only take the first index in the tuple
        
        top_nums = [num[0] for num in count_nums.most_common(k)]
        
        return top_nums