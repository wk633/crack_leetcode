def countNumbersWithUniqueDigits(n):
    choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    product, result = 1, 1
    for i in range(n):
        product *= choices[i]
        result += product
    return result

print countNumbersWithUniqueDigits(0)
print countNumbersWithUniqueDigits(1)
print countNumbersWithUniqueDigits(2)
print countNumbersWithUniqueDigits(3)
print countNumbersWithUniqueDigits(4)
print countNumbersWithUniqueDigits(5)
