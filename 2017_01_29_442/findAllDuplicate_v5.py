class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rst = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                rst.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        return rst
