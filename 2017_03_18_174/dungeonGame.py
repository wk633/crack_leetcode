class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[0]*(cols+1) for i in range(rows+1)]

        for idx in range(cols+1):
            dp[rows][idx] = float('inf')
        for idx in range(rows+1):
            dp[idx][cols] = float('inf')

        dp[rows][cols-1] = 1
        dp[rows-1][cols] = 1

        for i in range(rows)[::-1]:
            for j in range(cols)[::-1]:
                dp[i][j] = max(min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j], 1)
        return dp[0][0]

# reference: https://discuss.leetcode.com/topic/52942/a-very-clean-and-intuitive-solution-with-explanation
# 
