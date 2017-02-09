# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd,even = ListNode(None), ListNode(None)
        oddhead, evenhead = odd, even

        # process two nodes every time
        while head and head.next:
            oddhead.next = ListNode(head.val)
            oddhead = oddhead.next
            head = head.next

            evenhead.next = ListNode(head.val)
            evenhead = evenhead.next
            head = head.next

        # process the case when the length is of odd number
        if head:
            oddhead.next = head
            oddhead = oddhead.next

        # connect two linked list
        oddhead.next = even.next

        return odd.next
