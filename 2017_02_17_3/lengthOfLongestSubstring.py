class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # two pointers method with hash
        dic = {}
        left = 0
        maxlength = 0
        for i in xrange(len(s)):
            if s[i] in dic and left <= dic[s[i]]:
                # left <= dic[s[i]] is to make sure the former character is within the substring
                left = dic[s[i]]+1
            else:
                maxlength = max(maxlength, i-left+1)
            dic[s[i]] = i
        return maxlength

        # slide window
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
