def removeKdigits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    if len(num) == k:
        return '0'
    stack = []
    for item in num:
        while k and stack and item < stack[-1]:
            stack.pop()
            k -= 1
        stack.append(item)
        print "after process: ", stack
    return "".join(stack)

print removeKdigits("10", 1)
