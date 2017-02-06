# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        v1, v2 = 0, 0
        while l1:
            v1 *= 10
            v1 += l1.val
            l1 = l1.next
        while l2:
            v2 *= 10
            v2 += l2.val
            l2 = l2.next
        v = v1 + v2

        l = None
        while v:
            tmp = ListNode(v%10)
            v = v // 10
            tmp.next = l
            l = tmp
        return l if l else ListNode(0)
