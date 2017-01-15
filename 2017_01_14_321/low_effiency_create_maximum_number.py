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

def maxListNumber(nums, length):
    rst = []
    numsLength = len(nums)
    for numsIdx,numsItem in enumerate(nums):
        numsLeftLength = numsLength - 1 - numsIdx # this is used to indicate whether possible renew
        # iterate every item in rst
        renewFlag = False
        for rstIdx, rstItem in enumerate(rst):
            rstLeftLength = length - 1 - rstIdx
            if numsItem > rstItem and numsLeftLength >= rstLeftLength:
                renewFlag = True
                rst = rst[:rstIdx]
                rst.append(numsItem) # update rst
                # print rst
                break

        # if can not update rst then append this item to rst
        if not renewFlag and len(rst) < length:
            rst.append(numsItem)
    return rst

def mergeMax(list1, list2, totalLength):
    rst = []
    for i in xrange(totalLength):
        if (not list1) and list2 :
            # list1 is empty and list2 not
            rst += list2
            break
        if (not list2) and list1:
            # list2 empty and list2 not
            rst += list1
            break

        if list1[0] > list2[0]:
            # print "list1[0]: %s, list2[0]: %s, list1[0] > list2[0]" % (list1[0], list2[0])
            rst.append(list1[0])
            list1 = list1[1:]
        elif list1[0] < list2[0]:
            # print "list1[0]: %s, list2[0]: %s, list1[0] < list2[0]" % (list1[0], list2[0])
            rst.append(list2[0])
            list2 = list2[1:]
        else:
            # to address the equal case, we should use a bigger list first
            # for example [6,7], [6,0,4], it's better to use 6 in [6,7]
            if list1 > list2:
                rst.append(list1[0])
                list1 = list1[1:]
            else:
                rst.append(list2[0])
                list2 = list2[1:]

    return rst

# print 'nums1=[3,4,6,5], nums2=[9,1,2,5,8,3], k=5, rst: ', maxNumber([3,4,6,5], [9,1,2,5,8,3], 5)
# print 'nums1=[6,7], nums2=[6,0,4], k=5, rst: ', maxNumber([6,7], [6,0,4], 5)
# print 'nums1=[3,9], nums2=[8,9], k=3, rst: ', maxNumber([3,9], [8,9], 3)
print maxNumber([5,6,8], [6,4,0],3)
