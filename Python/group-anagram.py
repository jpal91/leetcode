# Time: O(n log(n))
# Space: O(n)
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Initialize Default Dict with empty list as value and response list for return
        sorted_dict = defaultdict(list)
        res = []
        
        # First, go through list and sort each word lexicographically this will become the key in sorted_dict
        # As each word is sorted, the anagrams will be added to the same list within sorted_dict

        for word in strs:
            sort_word = sorted(word) # sorted(str) returns list
            sort_word = "".join(sort_word) # convert list to str
            
            sorted_dict[sort_word].append(word)
        
        # Finally iterate through sorted_dict and add each list corresponding to the sorted key to res

        for key in sorted_dict:
            res.append(sorted_dict[key])
        
        return res