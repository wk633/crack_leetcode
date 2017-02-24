class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s.startswith("0"):
            return 0
        stack = [1, 1]
        for i in xrange(1, len(s)):
            if s[i] == "0":
                # one impossible case
                if s[i-1] == "0" or s[i-1] > '2':
                    return 0
                stack.append(stack[-2])
            elif 9 < int(s[i-1:i+1]) < 27:
                stack.append(stack[-2]+stack[-1])
            else:
                stack.append(stack[-1])
        return stack[-1]
        
