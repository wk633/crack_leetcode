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
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        stack3 = []
        carry = 0
        while len(stack1) > 0 or len(stack2) > 0:
            sum = carry
            if len(stack1) > 0:
                sum += stack1.pop()
            if len(stack2) > 0:
                sum += stack2.pop()
            carry = sum / 10
            stack3.append(sum % 10)
        if carry > 0:
            stack3.append(carry)
        stack3 = stack3[::-1]

        head = ListNode(0) # set a dumb head
        head2 = head
        for i in xrange(len(stack3)):
            head2.next = ListNode(stack3[i])
            head2 = head2.next

        return head.next
        
