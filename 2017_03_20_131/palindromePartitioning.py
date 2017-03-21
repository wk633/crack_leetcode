class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)

    def isPalindrome(self, s):
        start, end = 0, len(s)-1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

# reference: https://discuss.leetcode.com/topic/33425/python-recursive-iterative-backtracking-solution
