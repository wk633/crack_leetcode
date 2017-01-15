# -*- coding:utf-8 -*-

def maxNumber(nums1, nums2, k):
    length1, length2 = len(nums1), len(nums2)
    ret = [0]*k
    for len1 in range(0, k+1):
        len2 = k - len1
        if len1 > length1 or len2 > length2:
            continue
        list1 = maxListNumber(nums1, len1)
        list2 = maxListNumber(nums2, len2)
        num = mergeMax(list1, list2, k)
        ret = max(num, ret)
    return ret

def maxListNumber(nums, selects):
    rangeStart = 0
    rangeEnd = len(nums) - selects + 1
    n = selects # digits left to be selected
    rst = []
    while n > 0:
        idx = max(xrange(rangeStart, rangeEnd), key=nums.__getitem__) # 获得的是最大值的index，两个目标同时达成
        rangeStart = idx + 1
        rst.append(nums[idx])
        n -= 1
        rangeEnd = len(nums)-n+1
    return rst
# better mergeMax func
def mergeMax(list1, list2, totalLength):
    return [max(list1,list2).pop(0) for _ in xrange(totalLength)]

print 'nums1=[3,4,6,5], nums2=[9,1,2,5,8,3], k=5, rst: '
print maxNumber([3,4,6,5], [9,1,2,5,8,3], 5)
# print 'nums1=[6,7], nums2=[6,0,4], k=5, rst: ', maxNumber([6,7], [6,0,4], 5)
# print 'nums1=[3,9], nums2=[8,9], k=3, rst: ', maxNumber([3,9], [8,9], 3)
