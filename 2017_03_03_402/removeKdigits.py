class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        stack = []
        for item in num:
            while k and stack and item < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(item)
        return "".join(stack[:(len(stack),-k)[k!=0]]).lstrip("0") or "0"
