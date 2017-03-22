class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst = [[]]
        for num in nums:
            rst += [item + [num] for item in rst]
        return rst
# help understanding: https://discuss.leetcode.com/topic/30867/simple-iteration-no-recursion-no-twiddling-explanation
# different version of answers: https://discuss.leetcode.com/topic/19561/python-easy-to-understand-solutions-dfs-recursively-bit-manipulation-iteratively
