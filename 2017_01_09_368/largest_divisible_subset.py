def largestDivisibleSubset(nums):
    S = {-1: set()}
    for x in sorted(nums):
        S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
    return list(max(S.values(), key=len))
print largestDivisibleSubset([1,2,3,5,89,9,76,23,12])
