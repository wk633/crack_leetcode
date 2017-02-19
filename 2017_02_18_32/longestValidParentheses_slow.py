class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        left, right = 0, 0
        rst = 0
        count = 0
        # iterate from left to right find longest balance valid string
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            if s[i] == ")":
                right += 1
            if left == right:
                count += left
                left, right = 0, 0
            if right > left:
                left, right = 0, 0
                count = 0
            rst = max(rst, 2*count)

        count = 0
        left, right = 0, 0

        # iterate from right to left find longest balance substring
        for i in range(len(s)-1,-1,-1):
            if s[i] == "(":
                left += 1
            if s[i] == ")":
                right += 1
            if left == right:
                count += left
                left, right = 0, 0
            if left > right:
                left, right = 0, 0
                count = 0
            rst = max(rst, 2*count)
        return rst
