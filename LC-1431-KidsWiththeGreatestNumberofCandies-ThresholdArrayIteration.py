# Date Completed
# September 30, 2026

# Approach
# To determine if a child can have the greatest number of candies, 
# we set a threshold: max(candies) - extraCandies. 
# Any child whose current candy count is less than this threshold fails the condition, 
# as adding extraCandies will still leave them short of the current maximum.

# Time complexity:
# O(N)

# Space complexity:
# O(1)

# Code
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        largestNum = max(candies)
        largestNum -= extraCandies
        for i in range(len(candies)):
            if candies[i] >= largestNum:
                candies[i] = True
            else:
                candies[i] = False

        return candies

        
