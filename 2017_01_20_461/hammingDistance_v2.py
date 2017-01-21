def hammingDistance(x, y):
    ans = 0
    while x or y:
        ans += (x % 2) ^ (y % 2)
        x /= 2
        y /= 2
    return ans
