# -*- coding:utf-8 -*-

def numSquares(n):
    if n<2:
        return n
    i = 1
    lst = []
    while i*i <= n:
        lst.append(i*i)
        i += 1
    cnt = 0
    rootsToCheck = {n}
    while rootsToCheck:
        # 遍历从rootsToCheck每个元素开始，找到下一层所有可能的剩余值
        # 因为只关心多少层，所以只需要用集合来操作
        cnt += 1
        temp = set()
        for start_left in rootsToCheck:
            for possible_choice in lst:
                if start_left == possible_choice:
                    return cnt
                if start_left < possible_choice:
                    break # 看lst的生成过程，是一个从小到大的数组
                temp.add(start_left - possible_choice)
        rootsToCheck = temp
    return cnt

print numSquares(4)
print numSquares(10)
print numSquares(12)
