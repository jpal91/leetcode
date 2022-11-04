# Time: O(1)
# Space: O(n)
# https://leetcode.com/problems/design-front-middle-back-queue

class DLL:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class FrontMiddleBackQueue:

    def __init__(self):
        """
        Initializing two doubly linked lists for the left half
        and right half of the lists (l and r) and setting
        length properties for both
        """
        
        self.head_l = DLL(-1)
        self.tail_l = DLL(-2)
        self.head_l.next = self.tail_l
        self.tail_l.prev = self.head_l
        
        self.head_r = DLL(-3)
        self.tail_r = DLL(-4)
        self.head_r.next = self.tail_r
        self.tail_r.prev = self.head_r
        
        self.n_l = 0
        self.n_r = 0
        

    def pushFront(self, val: int) -> None:
        """
        Pushes to the front of the left half (l) DLL
        """
        node = DLL(val)
        node.next = self.head_l.next
        node.prev = self.head_l
        self.head_l.next.prev = node
        self.head_l.next = node
        self.n_l += 1
        
        self.balance()

    def pushMiddle(self, val: int) -> None:
        """
        Creates a new node and pushes the new node to
        the middle of the list. This is determined by the 
        length of either list. 
        
        We want to keep the lists
        either equal to eachother or with the right list
        having one extra in general so that a push to the middle
        will automatically go to the front of the current middle
        """
        node = DLL(val)
        
        if self.n_l < self.n_r:
            node.next = self.tail_l
            node.prev = self.tail_l.prev
            
            self.tail_l.prev.next = node
            self.tail_l.prev = node
            
            self.n_l += 1
        else:
            node.next = self.head_r.next
            node.prev = self.head_r
            
            self.head_r.next.prev = node
            self.head_r.next = node
            
            self.n_r += 1

    def pushBack(self, val: int) -> None:
        """
        Pushes to the back of the right list
        """
        node = DLL(val)
        node.next = self.tail_r
        node.prev = self.tail_r.prev
        self.tail_r.prev.next = node
        self.tail_r.prev = node
        self.n_r += 1
        
        self.balance()

    def popFront(self) -> int:
        """
        Pops from the front of the list. In this function the front is
        determined first by if both lists are empty, then if the left list
        is empty - go to the first of the right, finally if both have nodes,
        we'll pop from the front of the left as that is the true front of the list
        """
        if self.head_l.next.val == -2 and self.head_r.next.val == -4:
            return -1
        elif self.head_l.next.val == -2:
            val = self.head_r.next.val
            self.head_r.next.next.prev = self.head_r
            self.head_r.next = self.head_r.next.next
            self.n_r -= 1
        else:
            val = self.head_l.next.val
            self.head_l.next.next.prev = self.head_l
            self.head_l.next = self.head_l.next.next
            self.n_l -= 1
        
        self.balance()
        return val
        

    def popMiddle(self) -> int:
        """
        If the left list happens to be larger or both lists
        are equal, we will pop from the end of the left list as
        that would be the middle, else from the front of the right
        """
        if self.n_l >= self.n_r:
            if self.tail_l.prev.val == -1:
                return -1
            val = self.tail_l.prev.val
            self.tail_l.prev.prev.next = self.tail_l
            self.tail_l.prev = self.tail_l.prev.prev
            self.n_l -= 1
        else:
            if self.head_r.next.val == -4:
                return -1
            val = self.head_r.next.val
            self.head_r.next.next.prev = self.head_r
            self.head_r.next = self.head_r.next.next
            self.n_r -= 1
        
        return val

    def popBack(self) -> int:
        """
        Similar to popFront, checks if either list is empty, if one is empty
        - pop from the other, else pop from the back of the right
        """
        if self.tail_r.prev.val == -3 and self.tail_l.prev.val == -1:
            return -1
        elif self.tail_r.prev.val == -3:
            val = self.tail_l.prev.val
            self.tail_l.prev.prev.next = self.tail_l
            self.tail_l.prev = self.tail_l.prev.prev
            self.n_l -= 1
        else:
            val = self.tail_r.prev.val
            self.tail_r.prev.prev.next = self.tail_r
            self.tail_r.prev = self.tail_r.prev.prev
            self.n_r -= 1
        
        self.balance()
        return val
        
    def balance(self):
        """
        Self defined helper function to assist in balancing the list out.
        If there is one list that has more items than the other, we'll move
        the tail (left) or head (right) of the list and move it to the other
        
        The balancer makes sure that if possible, the right list has at least one
        more so that the push and pop methods for middle work properly
        """
        if self.n_l - self.n_r > 0:
            node = self.tail_l.prev
            self.tail_l.prev.prev.next = self.tail_l
            self.tail_l.prev = self.tail_l.prev.prev
            
            node.prev = self.head_r
            node.next = self.head_r.next
            
            self.head_r.next.prev = node
            self.head_r.next = node
            
            self.n_l -= 1
            self.n_r += 1
        elif self.n_r - self.n_l > 1:
            node = self.head_r.next
            self.head_r.next.next.prev = self.head_r
            self.head_r.next = self.head_r.next.next
            
            node.next = self.tail_l
            node.prev = self.tail_l.prev
            
            self.tail_l.prev.next = node
            self.tail_l.prev = node
            
            self.n_l += 1
            self.n_r -= 1

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
