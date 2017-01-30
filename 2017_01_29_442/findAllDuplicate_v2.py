# solution with extra space
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = dict()
        rst = []
        for item in nums:
            if item in dic:
                rst.append(item)
            else:
                dic[item] = 1
        return rst
