class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return sorted(s) == sorted(t)

        # dic1 = {}
        # dic2 = {}
        # for i in s:
        #     dic1[i] = dic1.get(i,0) + 1
        # for i in t:
        #     dic2[i] = dic2.get(i,0) + 1
        # return dic1 == dic2

        rst1 = [0]*26
        rst2 = [0]*26
        for i in s:
            rst1[ord(i)-ord("a")] += 1
        for i in t:
            rst2[ord(i)-ord("a")] += 1
        return rst1 == rst2
