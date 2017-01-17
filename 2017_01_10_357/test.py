def countNumbersWithUniqueDigits(n):
    counts = [9,9,8,7,6,5,4,3,2,1]
    if n == 0:
        return 1
    product, rst = 1, 1
    for i in range(n):
        product *= counts[i]
        rst += product
    return rst

print countNumbersWithUniqueDigits(0)
print countNumbersWithUniqueDigits(1)
print countNumbersWithUniqueDigits(2)
print countNumbersWithUniqueDigits(3)
print countNumbersWithUniqueDigits(4)
print countNumbersWithUniqueDigits(5)
