# Date Completed
# October 19, 2026

# Approach


# Time complexity:
# O(N)

# Space complexity:
# O(N)

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
        
        