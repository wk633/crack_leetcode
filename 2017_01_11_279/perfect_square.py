def numSquares(n):
    if n < 2:
        return n
    lst = []
    i = 1
    while i * i <= n:
        lst.append( i * i )
        i += 1
    print "lst: ", lst
    cnt = 0
    toCheck = {n}
    while toCheck:
        cnt += 1
        temp = set()
        print "toCheck: ", toCheck
        for x in toCheck:
            print "x: ",x
            for y in lst:
                print "y: ", y
                if x == y:
                    return cnt
                if x < y:
                    break
                temp.add(x-y)
                print "y: ", y
                print "temp: ", temp
        toCheck = temp

    return cnt
print numSquares(12)
