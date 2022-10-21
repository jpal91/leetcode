# Time: O(n)
# Space: O(n)
# https://leetcode.com/problems/flip-game

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        n = len(currentState)
        res = []
        
        # If there are less than two characters in the string, there are no valid moves
        if n < 2:
            return res
        
        # Iterate through the string checking the current index and the next index to see if both are +
        # If they are, append the string before the index + '--' + the string after the second index
        for i in range(n - 1):
            c1, c2 = currentState[i], currentState[i + 1]
            if c1 == c2:
                if c1 == '+':
                    res.append(currentState[:i] + '--' + currentState[i + 2:])
        
        return res