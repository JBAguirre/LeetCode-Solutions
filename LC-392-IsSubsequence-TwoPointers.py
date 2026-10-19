# Date Completed
# October 19, 2026

# Approach
# The algoritm uses two pointers to iterate through the list. The first pointer, i, keeps track of the position 
# where the next non-zero element should be placed. 
# The second pointer, j, iterates through the entire list. 
# When a non-zero element is found at index j, it is swapped with the element at index i, and i is incremented. 
# This effectively moves all non-zero elements to the front of the list while maintaining their relative order, 
# and all zeros are moved to the end.

# Time complexity:
# O(N)

# Space complexity:
# O(1)

# Code
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0

        for j in range(len(t)):
            if i < len(s) and s[i] == t[j]:
                i += 1
            
        return i == len(s)
        
        
        