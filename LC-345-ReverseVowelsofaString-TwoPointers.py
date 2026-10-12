# Date Completed
# October 3, 2026

# Approach
# Two pointers converge from the ends toward the middle.
# Both pointers traverse until both have vowels. Then, the vowels swap.
# After all swaps are finished, the array is converted back into a string.

# Time complexity:
# O(N)

# Space complexity:
# O(N)

# Code
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Convert the string into an array
        vowels = "aeiouAEIOU"
        word = list(s)

        # Set two pointers (l = left, r = right)
        l = 0
        r = len(word) - 1

        # Traverse both pointers towards the middle
        # If they meet in the middle then stop
        while l <= r:
            left = word[l] in vowels 
            right = word[r] in vowels
            temp = []
            if left and right == True:
                temp = word[l]
                word[l] = word[r]
                word[r] = temp
                l += 1
                r -= 1
            elif left == True:
                r -= 1
            else:
                l += 1

        # Convert the array back into a string
        return "".join(word)
        