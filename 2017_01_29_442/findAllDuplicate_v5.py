class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        rst = []
        for num in nums:
            if nums[(num % N) -1] <= N:
                nums[(num % N) -1] += N
            else:
                if num > N:
                    rst.append(num-N)
                else:
                    rst.append(num)

        return rst
