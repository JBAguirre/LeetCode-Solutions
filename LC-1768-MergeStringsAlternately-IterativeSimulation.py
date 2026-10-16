# Date Completed
# October 16, 2026

# Approach


# Time complexity:
# O(N)

# Space complexity:
# O(N)

# Code
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge_string = ""
        length = max(len(word1), len(word2))

        for i in range(length):
            if i < len(word1):
                merge_string += word1[i]
            if i < len(word2):
                merge_string += word2[i]

        return merge_string
        
        