def findSubstringInWraproundString(p):
    """
    :type p: str
    :rtype: int
    """
    pLength = len(p)
    if pLength == 0:
        return 0
    counts = [0]*26
    maxLength = 1
    counts[ord(p[0])-ord("a")] = 1

    for i in xrange(1, pLength):
        ordPre = ord(p[i-1])
        ordCur = ord(p[i])
        if ordPre+1 == ordCur or ordPre-25 == ordCur:
            maxLength += 1
        else:
            maxLength = 1
        counts[ordCur- ord("a")] = max(maxLength, counts[ordCur-ord("a")])

    return sum(counts)
print findSubstringInWraproundString("aca")
print findSubstringInWraproundString("zab")
