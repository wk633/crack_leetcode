class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        s = "+" + s.strip() + "+"
        d = 0
        op = ""
        opSet = set(["+", "-", "*", "/"])
        tmp = []

        for item in s:
            if item.isdigit():
                d = d*10 + int(item)
                continue
            if item in opSet:
                if op == "+":
                    tmp.append(d)
                if op == "-":
                    tmp.append(-1*d)
                if op == "*":
                    tmp[-1] = tmp[-1]*d
                if op == "/":
                    if tmp[-1] < 0:
                        tmp[-1] = -1 * (-1 * tmp[-1] / d)
                    else:
                        tmp[-1] = tmp[-1] / d

                op = item
                d = 0
        return sum(tmp)
