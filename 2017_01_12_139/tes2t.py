def wordBreak(s, wordDict):
    rst = [False] * len(s)
    for i in xrange(len(s)):
        for w in wordDict:
            if len(w) > i+1:
                continue

            if s[i+1-len(w):i+1] == w and (i-len(w)== -1 or rst[i-len(w)]==True):
                rst[i] = True
    return rst[-1]

s = "leetcode"
words = ["leet", 'code']
print wordBreak(s, words)
