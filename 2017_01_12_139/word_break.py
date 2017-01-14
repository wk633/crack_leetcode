
def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    d = [False] * len(s)

    for i in xrange(len(s)):
      for w in wordDict:
        if (i - len(w) < -1):
          continue
        if w == s[i - len(w) + 1:i + 1] and (i - len(w) == -1 or d[i - len(w)] == True):
          d[i] = True
    return d[-1]

s = "leetcode"
words = ["leet", 'code']
print wordBreak(s, words)
