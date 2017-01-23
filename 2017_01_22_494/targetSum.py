class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        count = collections.defaultdict(int)
        count[0] = 1
        for item in nums:
            step = collections.defaultdict(int)
            for y in count:
                step[y+item] += count[y]
                step[y-item] += count[y]
            count = step
        return count[S]
