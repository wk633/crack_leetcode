class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        rst = 0
        left = -1  # left index to compare
        for i in xrange(len(s)):
            if s[i] == "(":
                if left == -1:
                    # haven't been matched yet
                    stack.append(i)
                else:
                    # indicate that it's possible to match longer length string
                    stack.append(left)
                    left = -1
            else:
                if stack:
                    left = stack.pop() # after match left value will change
                    rst = max(i-left+1, rst)
                else:
                    left = -1
        return rst
