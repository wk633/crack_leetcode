class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        rst = [1]
        vlist = [1]*len(primes)
        idxlist = [0]*len(primes)
        umin = 1
        while n > 1:
            for i in xrange(len(vlist)):
                if umin == vlist[i]:
                    vlist[i] = rst[idxlist[i]] * primes[i]
                    idxlist[i] += 1

            umin = min(vlist)
            n -= 1
            rst.append(umin)
        return rst[-1]
