import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        list1, list2 = nums1[:k], nums2[:k]
        return heapq.nsmallest(k, ([num1, num2] for num1 in nums1 for num2 in nums2), key=sum)
