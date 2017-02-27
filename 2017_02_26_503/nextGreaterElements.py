class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        stack, rst = [], [-1]*len(nums)
        for i in xrange(-len(nums), len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                rst[stack.pop()] = nums[i]
            if i < 0:
                stack.append(i)
        return rst
