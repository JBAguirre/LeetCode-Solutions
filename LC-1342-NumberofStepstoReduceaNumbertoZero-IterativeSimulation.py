# Date Completed
# June 27, 2026

# Approach
# There are only two conditions set to reach to zero: divide if it is even, and subtract if it is odd. 
# I set an if-else statement for the two conditions while having the variable of step to increment in every conditions satified.

# Time complexity:
# O(log N)

# Space complexity:
# O(1)

# Code
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        step = 0

        while num != 0:
            if num % 2 == 0:
                num = num/2
                step += 1
            elif num % 2 != 0:
                num -= 1
                step += 1
        return step