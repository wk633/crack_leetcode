# -*- coding:utf-8 -*-

def wordBreak(s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = [False]*len(s)

        for i in xrange(len(s)):
            for w in wordDict:
                if (i - len(w) < -1):
                    continue
                print "w: ", w
                print "i: ",i
                print "单词尾与s[i]匹配的子字符串 s[i-len(w)+1:i+1]:", s[i-len(w)+1:i+1]
                if w == s[i-len(w)+1:i+1] and (i - len(w) == -1 or d[i-len(w)]==True):
                    print "匹配成功"
                    d[i] = True
                    print "d: ",d,"\n"
        print d
        return d[-1]
s = "leetcode"
words = ["leet", 'code']
print wordBreak(s, words)
