# Time: O(n log(n))
# Space: O(n)
# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
        # We would want to be greedy and try to fill the 
        # category with the highest number of cups needed to 
        # be filled first, so we initialize a heapq with 
        # negative numbers in order to take the highest first
        
        cups = [-a for a in amount if a > 0]
        heapq.heapify(cups)
        count = 0
        
        # While there are still cups in the queue (before all are 0)
        # We will take 1-2 cups out of the queue with the highest counts
        # and subtract them by 1, then add them back into the queue
        # We will always take the most optimal row as the heapq will take the
        # lowest(highest in this case) out first
        
        while cups:
            cup = heapq.heappop(cups) + 1
            second_cup = heapq.heappop(cups) + 1 if cups else None
                
            
            if cup < 0:
                heapq.heappush(cups, cup)
            if second_cup and second_cup < 0:
                heapq.heappush(cups, second_cup)

            
            count += 1
            
        return count
