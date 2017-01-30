class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rst = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                continue
            else:
                nums[abs(num)-1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                rst.append(i+1)
        return rst
## not efficient
