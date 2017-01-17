# -*- coding:utf-8 -*-

def numSquares(n):
    i = 1
    choiceList = []
    while i*i <= n:
        choiceList.append(i*i)
        i += 1
    layCount = 0
    currentSet = {n}
    while currentSet:
        temp = set()
        layCount += 1
        for i in currentSet:
            for j in choiceList:
                if j > i:
                    break
                elif i == j:
                    return layCount
                else:
                    temp.add(i-j)
        currentSet = temp

print numSquares(4)
print numSquares(10)
print numSquares(12)
