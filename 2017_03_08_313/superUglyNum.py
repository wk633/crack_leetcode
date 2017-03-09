class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        rst = [1]
        idxList = [0]*len(primes)
        while n > 1:
            tmp = [rst[idxList[i]]*primes[i] for i in xrange(len(primes))]
            minValue = min(tmp)

            for i in xrange(len(tmp)):
                if tmp[i] == minValue:
                    idxList[i] += 1
            rst.append(minValue)
            n -= 1
        return rst[-1]
