# Time: O(n)
# Space: O(n)
# https://leetcode.com/problems/map-sum-pairs/

class Trie:
    def __init__(self, val = None, letter = None):
        self.val = val
        self.children = {}
        self.letter = letter
        
class MapSum:

    def __init__(self):
        """
        Initialize a root Trie and a dict to track the values
        of each inserted word 
        """
        self.root = Trie()
        self.dict = {}

    def insert(self, key: str, val: int) -> None:
        """
        Goes through each letter within the Trie and either
        updates the value associated with an existing Trie node
        by adding the current value to the new value or adding
        a new node with new value provided
        
        If the key was already added in, instead of strictly creating
        or updating a node by adding the new value, first we find the differnce
        from the old and new value of the particular key and add that to each
        subsequent node instead
        """
        node = self.root.children
        new_val = val
        
        if key in self.dict:
            val = (val - self.dict[key])
        
        for k in key:
            if k in node:
                node[k].val += val
            else:
                node[k] = Trie(val, k)
            node = node[k].children
        
        self.dict[key] = new_val

    def sum(self, prefix: str) -> int:
        """
        Traverses the Trie using the prefix and updating
        the total based on each subsequent letters value.
        
        At the end, if the letter doesn't exist, the total
        is zero as the prefix doesn't exist. Else, the total
        is the value of the last letter in the prefix
        """
        node = self.root.children
        total = 0
        
        for p in prefix:
            if p in node:
                total = node[p].val
                node = node[p].children
            else:
                total = 0
                break
        
        return total
    
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
