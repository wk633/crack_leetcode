class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
        maxLength = 0

        for num in nums:
            tempLength = 1
            tmp = num
            # find consecutive elements from both side, then compare the max length
            while (tmp-1 in dic):
                tempLength += 1
                tmp -= 1
                del dic[tmp]

            while num+1 in dic:
                tempLength += 1
                num += 1
                del dic[num]

            maxLength = max(maxLength, tempLength)
        return maxLength
