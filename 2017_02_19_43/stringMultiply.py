class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product = [0]*(len(num1)+len(num2))
        for i, digit1 in enumerate(reversed(num1)):
            for j, digit2 in enumerate(reversed(num2)):
                product[i+j] += (ord(digit1)-ord("0"))*(ord(digit2)-ord("0"))
                product[i+j+1] += product[i+j] / 10
                product[i+j] %= 10

        return "".join(map(str, product[::-1])).lstrip("0") or "0"
