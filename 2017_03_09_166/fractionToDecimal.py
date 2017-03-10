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
        remainderStack = []
        while remainder not in remainderStack:
            remainderStack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            rst.append(str(n))
        idx = remainderStack.index(remainder)
        rst.insert(idx+2, "(")
        rst.append(")")

        return "".join(rst).replace("(0)", "").rstrip(".")
        
