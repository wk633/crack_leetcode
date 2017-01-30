class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rst = []
        for num in nums:
            if num < 0:
                if nums[-num-1] < 0:
                    rst.append(-num)
                else:
                    nums[-num-1] *= -1
            else:
                if nums[num-1] < 0:
                    rst.append(num)
                else:
                    nums[num-1] *= -1
        return rst
