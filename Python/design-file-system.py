# Time: O(T) - Based on the number of nodes that exist in the tree
# Space: O(T)
# https://leetcode.com/problems/design-file-system

# Initiate a TrieNode class which stores the path, value of the path (if any)
# and the child paths
class TrieNode:
    def __init__(self, path, val = None):
        self.path = path
        self.val = val
        self.children = {}

class FileSystem:
    def __init__(self):
        # Initializes a "root" TrieNode directory
        self.dir = TrieNode('/')

    def createPath(self, path: str, value: int) -> bool:
        
        # Split each given path by '/' to show each parent and sub
        # directory within a list. This method will always have a 
        # None string as the first index, so delete
        sp_path = path.split('/')
        del sp_path[0]
        n = len(sp_path)
        
        if not sp_path[0]:
            return False
        elif n > 1 and sp_path[0] not in self.dir.children:
            return False
        
        node = self.dir
        
        # Go through the directory and check if each path exists already
        # If we get to a path where the sub-directory doesn't exist and we're 
        # not at the end of our path, we can return False. If we're at the end of
        # our path directory and assuming a value hasn't already been assigned, we 
            create
        # the new sub directory and assign it the value given
        
        for i in range(n):
            if i == n - 1:
                if sp_path[i] in node.children and node.children[sp_path[i]].val:
                    return False
                node.children[sp_path[i]] = TrieNode(sp_path[i], value)
            elif sp_path[i] not in node.children:
                return False
            node = node.children[sp_path[i]]
        
        return True

    def get(self, path: str) -> int:
        sp_path = path.split('/')
        del sp_path[0]
        n = len(sp_path)
        
        if sp_path[0] not in self.dir.children:
            return -1
        
        node = self.dir
        
        # We move through the directory similar to how we did in create
        # each time checking if a path exists and if it does, move into the 
        # sub directory
        # Once we reach the end, we return the value associated with the sub 
            directory
        
        for i in range(n):
            if sp_path[i] not in node.children:
                return -1
            node = node.children[sp_path[i]]
            if i == n - 1:
                return node.val
            


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)

