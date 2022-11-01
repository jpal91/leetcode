# Time O(n)
# Space O(1)
# https://leetcode.com/problems/time-needed-to-buy-tickets

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # The minimum number of seconds will be equal to the number
        # of tickets the person is requesting at the k index, so we
        # will start our count with this amount and create a variable
        # for this number of tickets to compare to others in the queue
        
        min_tix, count = tickets[k], tickets[k]
        
        # Iterating over the first part of the list (prior to index k),
        # we will take the lesser of the number of tickets this person
        # is requesting or the number of tickets k index wants, as the 
        # purchasing must be done in order, anyone that wants tickets prior
        # to k will be fufilled
        
        # Once we reach the second half of the list, we need to factor in
        # that once k receives all of their tickets, we will not have to 
        # add any more tickets from the people behind. However, while k
        # still needs tickets, they will have to be counted as well
        
        # We simulate this through checking if people behind need the
        # same amount or more of tickets, if so we take this number minus 1
        # as we won't need that last ticket once k is done. Altertively, we'll
        # just take the number of tickets requested as they are lesser and we will
        # have to take them all anyway as we loop
        
        for i, t in enumerate(tickets):
            if i == k:
                continue
            elif i > k:
                if t >= min_tix:
                    count += min_tix - 1
                else:
                    count += t
            else:
                count += min(min_tix, t)
                
        
        return count
        
        
        
