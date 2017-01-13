# -*- coding:utf-8 -*-

# 升级： 输出最短数组
def numSquares(n):
    if n < 2:
        return n
    i = 1
    lst = []
    while i*i <= n:
        lst.append(i*i)
        i += 1

    rootsToCheck = {}
    resultlst = []
    


numSquares(10)
