class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1, ptr2 = 0, 0
        n1, n2 = len(word1), len(word2)
        # n = max(n1, n2)
        first = True
        res = ''
        
        while ptr1 < n1 or ptr2 < n2:
            if ptr1 >= n1:
                res += word2[ptr2]
                ptr2 += 1
            elif ptr2 >= n2:
                res += word1[ptr1]
                ptr1 += 1
            elif first:
                res += word1[ptr1]
                ptr1 += 1
            else:
                res += word2[ptr2]
                ptr2 += 1
            
            first = not first
        
        return res

#         for i, j in zip(range(n1), range(n2)):
#             res += word1[i]
#             res += word2[j]
        
#         if n1 > n2:
#             res += word1[i + 1:]
#         elif n2 > n1:
#             res += word2[j + 1:]
        
#         return res

#         for i in range(n):
#             if i < n1 and i < n2:
#                 res += word1[i]
#                 res += word2[i]
#             elif i >= n1:
#                 res += word2[i]
#             elif i >= n2:
#                 res += word1[i]
        
#         return res
