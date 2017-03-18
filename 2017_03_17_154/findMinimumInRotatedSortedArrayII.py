class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        i, j = 0, len(nums)-1
        while i < j:
            mid = i + (j - i) / 2
            if nums[mid] > nums[j]:
                i = mid + 1
            elif nums[mid] < nums[j]:
                j = mid
            else:
                j = j - 1 # for case [3,3,1,3]
        return nums[i]
