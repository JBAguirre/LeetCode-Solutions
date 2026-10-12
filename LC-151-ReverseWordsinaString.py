# Date Completed
# October 4, 2026

# Approach
# The string is split into an array of words while removing any extra spaces. 
# The .reverse() function the reverse the order of the words in the array. 
# The words are then joined back together into a single string, separated by a single space.

# Time complexity:
# O(N)

# Space complexity:
# O(N)

# Code
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s.split()
        s.reverse()
        return " ".join(s)
