class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        candicate1, candicate2, n1, n2 = float('inf'),float('inf'),0,0
        for num in nums:
            if num == candicate1:
                n1 += 1
            elif num == candicate2:
                n2 += 1
            elif n1 == 0:
                candicate1 = num
                n1 += 1
            elif n2 == 0:
                candicate2 = num
                n2 += 1
            else:
                n1, n2 = n1 - 1, n2 -1
        rst = []
        minlength = len(nums)/3
        if nums.count(candicate1) > minlength:
            rst.append(candicate1)
        if nums.count(candicate2) > minlength:
            rst.append(candicate2)
        return rst
