class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.dfs(n, n, "", [])

    def dfs(self, left, right, s, rst):
        # end condition
        if left == 0 and right == 0:
            rst.append(s)
        # consume left bracket is ok
        if left > 0:
            self.dfs(left-1, right, s+"(", rst)
        #  if consume right bracket, should have more right one than left one
        if right > 0 and right > left:
            self.dfs(left, right-1, s+")", rst)
        return rst
