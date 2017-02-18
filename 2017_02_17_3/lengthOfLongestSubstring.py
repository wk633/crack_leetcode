class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # queue = []
        # rst = 0
        # for i in xrange(len(s)):
        #     if s[i] not in queue:
        #         queue.append(s[i])
        #     else:
        #         rst = max(rst, len(queue))
        #         idx = queue.index(s[i])
        #         queue = queue[idx+1::]
        #         queue.append(s[i])
        # return max(rst, len(queue))

        tmp = ""
        rst = 0
        for i in xrange(len(s)):
            idx = tmp.find(s[i])
            tmp = tmp[idx+1::] + (s[i])
            rst = max(len(tmp), rst)
        return rst
