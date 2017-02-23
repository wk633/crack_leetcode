class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag, rst = 1,0
        for item in s:
            if item != " " and flag:
                # start of a segment
                rst += 1
                flag = 0
            elif item == " ":
                # end of a segment
                flag = 1
        return rst
