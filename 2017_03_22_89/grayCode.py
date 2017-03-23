ass Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        rst = [0]
        for i in range(n):
            rst += [item+pow(2, i) for item in reversed(rst)]
        return rst
# reference: https://discuss.leetcode.com/topic/4883/one-liner-python-solution-with-demo-in-comments
