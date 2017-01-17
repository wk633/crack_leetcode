class NumArray(object):
    def __init__(self, nums):
        self.dp = [nums[0]]
        for i in range(1, len(nums)):
            self.dp.append(self.dp[-1]+nums[i])

    def sumRange(self, i, j):
        return self.dp[j]-self.dp[i-1] if i != 0 else self.dp[j]

nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)
print numArray.sumRange(0,1)
print numArray.sumRange(2,4)
