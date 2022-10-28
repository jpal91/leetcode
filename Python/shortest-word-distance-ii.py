# Time: O(n)
# Space: O(n)
# https://leetcode.com/problems/shortest-word-distance-ii

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        # Since we're potentially working with duplicates, we initiate a defaultdict
        # with lists. Each index of the word will be stored within and accessible by key
        
        self.hash = defaultdict(list)
        
        for i, w in enumerate(wordsDict):
            self.hash[w].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        w1, w2 = self.hash[word1], self.hash[word2]
        t, b = 0, 0
        n_t, n_b = len(w1), len(w2)
        min_dist = float('inf')
        
        # We first get each list associated with the respective word
        # Then we will use two pointers to iterate over both lists simultaneously
        # If both words are unique, there's only one index to compare and the return will happen
        # after the first iteration.
        #
        # If there are duplicates in either table, the pointers will go through comparing the absolute
        # difference between either index. If the first index is higher than the second, the second pointer
        # will be moved up (and vice versa). Since these indices were appended in ascending order, we know that
        # the next index should be higher than the last. We want to attempt to get the numbers as close as possible to
        # one another to find the lowest abs difference
        
        while t < n_t or b < n_b:
            min_dist = min(min_dist, abs(w1[t] - w2[b]))
            
            if min_dist == 1:
                return 1
            
            if t == n_t - 1 and b == n_b - 1:
                break
            
            if t == n_t - 1:
                b += 1
            elif b == n_b - 1:
                t += 1
            elif w1[t] > w2[b]:
                b += 1
            elif w1[t] < w2[b]:
                t += 1

        
        return min_dist
                


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
