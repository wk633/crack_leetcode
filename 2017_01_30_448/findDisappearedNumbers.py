class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rst = []
        N = len(nums)
        for num in nums:
            nums[(num % N) -1] += N

        return [i+1 for i in range(N) if nums[i]<=N]
