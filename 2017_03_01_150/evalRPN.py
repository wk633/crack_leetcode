class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operations = {"+": lambda x,y: x+y, "-": lambda x,y:y-x, "*":lambda x,y:x*y, "/":lambda x,y: y/x}
        for item in tokens:
            if item in operations:
                stack.append(int(operations[item](stack.pop(), stack.pop())))
            else:
                stack.append(float(item))
        return int(stack.pop())
