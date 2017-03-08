class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        rst = [1]
        l1, l2, l3 = 0, 0, 0
        while n > 1:
            tmp1, tmp2, tmp3 = 2*rst[l1], 3*rst[l2], 5*rst[l3]
            umin = min(tmp1, tmp2, tmp3)
            if umin == tmp1:
                l1 += 1
            if umin == tmp2:
                l2 += 1
            if umin == tmp3:
                l3 += 1
            rst.append(umin)
            n -= 1
        return rst[-1]
