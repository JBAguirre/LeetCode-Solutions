# Date Completed
# October 2, 2026

# Approach
# Placement is determined by checking the values of adjacent plots:
# 1. Plots at the edge of the array (start/end) check only one neighbor.
# 2. Plots in the middle check both neighbors.
# If an adjacent plot has a flower (1), we skip to the next index.
# Returns True if all 'n' flowers are planted, and False otherwise.

# Time complexity:
# O(N)

# Space complexity:
# O(1)

# Code
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if (i == 0) or (flowerbed[i - 1] == 0):
                    if (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0):
                        n -= 1
                        flowerbed[i] = 1
                    else:
                        continue
                else:
                    continue
            else:
                continue

        if n <= 0:
            return True
        else:
            return False