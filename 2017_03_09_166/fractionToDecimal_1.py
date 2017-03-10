class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        sign = ""
        n, remainder = divmod(abs(numerator), abs(denominator))
        if((numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0)):
            sign = "-"

        rst = [sign+str(n), "."]
        

        remainderStack = {}
        i = 0
        while remainder not in remainderStack:
            remainderStack[remainder] = i
            n, remainder = divmod(remainder*10, abs(denominator))
            rst.append(str(n))
            i += 1

        idx = remainderStack[remainder]+2
        result = "".join(rst[:idx]) + "("+ "".join(rst[idx:]) + ")"
        return result.replace("(0)", "").rstrip(".")
