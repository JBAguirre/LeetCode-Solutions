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
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        temp = 0

        for j in range(len(nums)):
            if nums[i] == 0 and nums[j] != 0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                i += 1
            elif nums[i] != 0:
                i += 1
        
        