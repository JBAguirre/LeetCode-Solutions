# Date Completed
# October 19, 2026

# Approach
# The algorithm uses two pointers to iterate through the strings. 
# The first pointer, i, keeps track of the position in string s, while the second pointer, j, iterates through string t. 
# When a character in t matches the current character in s (s[i]), the pointer i is incremented to check for the next character 
# in s. If all characters in s are found in t in order, the function returns True; otherwise, it returns False.

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