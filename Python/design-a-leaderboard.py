# Space: O(n)
# https://leetcode.com/problems/design-a-leaderboard

class Leaderboard:

    def __init__(self):
        """
        Initializes a default dict which will store player scores
        """
        self.scores = defaultdict(int)
    
    # Time O(n)
    def addScore(self, playerId: int, score: int) -> None:
        """
        Updates each players score with the associated id as the key
        """
        self.scores[playerId] += score
    
    # Time O(n log(n))
    def top(self, K: int) -> int:
        """
        Sorts the scores dict in reverse by values, slices to take the top K,
        and returns the sum of these values.
        
        After trying out multiple options (see top2, top3), the simplest
        won out by a landslide (at least by runtime on LC). Ultimately the other
        two options have roughly the same time complexity but I believe by adding
        on the extra lookups to the dict, plus sorting, plus inserting, the other
        options are going through far more steps than this simple one-liner
        """
        
        return sum(sorted(self.scores.values(), reverse = True)[:K])
    
    # Time O(n log(n))
    def top2(self, K: int) -> int:
        """
        Alternate attempt to top using bisect.
        """
        lb = []
        
        for s in self.scores:
            score = self.scores[s]
            bisect.insort_left(lb, score, key = lambda x: -x)
        
        return sum(lb[:K])
    
    # Time O(n log(n))
    def top3(self, K: int) -> int:
        """
        Alternate attempt to top using heapq
        """
        heap = []
    
        for s in self.scores:
            heapq.heappush(heap, self.scores[s])
            
        return sum(heapq.nlargest(K, heap))
    
    # Time O(n)
    def reset(self, playerId: int) -> None:
        """
        Remove id from scores dict
        """
        del self.scores[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
