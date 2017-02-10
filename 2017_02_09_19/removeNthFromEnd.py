# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        p = head
        for i in xrange(n):
            p = p.next

        q = dummy
        while p:
            p = p.next
            q = q.next
        q.next = q.next.next

        return dummy.next
