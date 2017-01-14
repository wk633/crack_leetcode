def integerBreak(n):
    if n < 2: return 0
    if n == 2: return 1
    if n == 3: return 2
    rst = 1
    while n > 4:
        rst *= 3
        n -= 3
    rst *= n
    return rst


print integerBreak(12)
