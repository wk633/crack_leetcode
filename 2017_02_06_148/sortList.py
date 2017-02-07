# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        midPoint = self.findMid(head)
        rightHead = midPoint.next
        midPoint.next = None

        return self.merge(self.sortList(head), self.sortList(rightHead))

    def findMid(self, head):
        # lenght 2 return 1st node
        # lenght 3 return 2nd node
        # lenght 4 return 2nd ndoe
        # length 5 return 3rd node
        # length 6 return 3rd node
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, head1, head2):
        dummy = ListNode(None)
        node = dummy
        while head1 and head2:
            if head1.val < head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next
        node.next = head1 or head2
        return dummy.next
                
