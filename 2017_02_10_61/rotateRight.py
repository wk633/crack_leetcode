# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head

        length = 1
        node = head
        while node.next:
            length += 1
            node = node.next
        node.next = head
        # currently node is at original tail node
        k = k % length
        for i in range(length-k):
            node = node.next
        rst = node.next
        node.next = None
        return rst
