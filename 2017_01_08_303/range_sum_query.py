class NumArray(object):
    def __init__(self, nums):
        if len(nums)==0:
            return None
        self.dp = [nums[0]]
        for i in xrange(1, len(nums)):
            self.dp.append(self.dp[i-1]+nums[i])
    def sumRange(self, i, j):
        return self.dp[j] - (self.dp[i-1] if i > 0 else 0)

nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)
print numArray.sumRange(0,1)
print numArray.sumRange(2,4)
