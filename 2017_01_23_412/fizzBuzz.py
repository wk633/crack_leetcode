class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rst = []
        for i in xrange(1,n+1):
            if i%3 == 0 and i%15 !=0:
                rst.append("Fizz")
            elif i%5 == 0 and i%15 !=0:
                rst.append("Buzz")
            elif i%15 == 0:
                rst.append("FizzBuzz")
            else:
                rst.append(str(i))
        return rst
