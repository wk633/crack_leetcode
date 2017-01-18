class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLength = 0
        currentMax = 0
        for item in nums:
            if item != 0:
                maxLength += 1
            else:
                if maxLength > currentMax:
                    currentMax = maxLength
                maxLength = 0
        return max(currentMax, maxLength)
