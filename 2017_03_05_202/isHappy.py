class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = set()
        while n != 1:
            n = sum([int(num)**2 for num in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        return True
