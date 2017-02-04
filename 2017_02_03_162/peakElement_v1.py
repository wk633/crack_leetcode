class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n)
        nums = nums + [float('-inf')]
        for i in xrange(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
