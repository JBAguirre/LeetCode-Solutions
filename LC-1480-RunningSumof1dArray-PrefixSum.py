# Approach
# Since a running sum is just adding what came before it, 
# I took the sum from the previous index and 
# add it to the current index number.



# Time complexity:
# O(N)

# Space complexity:
# O(1)

# Code
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
                nums[i] = nums[i] + nums[i - 1]  
        
        return nums
        