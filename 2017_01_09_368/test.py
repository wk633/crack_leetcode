def largestDivisibleSubset(nums):
    rst = {-1: set()}
    for item in sorted(nums):
        rst[item] = max((rst[mm] for mm in rst if item%mm == 0), key=len) | {item}
    print rst
    return list(max(rst.values(), key=len))
print largestDivisibleSubset([1,2,3,5,89,9,76,23,12])
