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
        # v1, v2 = 0, 0
        # while l1:
        #     v1 *= 10
        #     v1 += l1.val
        #     l1 = l1.next
        # while l2:
        #     v2 *= 10
        #     v2 += l2.val
        #     l2 = l2.next
        # v = v1 + v2

        # l = None
        # while v:
        #     tmp = ListNode(v%10)
        #     v = v // 10
        #     tmp.next = l
        #     l = tmp
        # return l if l else ListNode(0)

        # stack1 = []
        # stack2 = []
        # while l1:
        #     stack1.append(l1.val)
        #     l1 = l1.next
        # while l2:
        #     stack2.append(l2.val)
        #     l2 = l2.next

        # stack3, carry, sum = [], 0, 0

        # while stack1 or stack2 or carry:
        #     sum = carry
        #     if len(stack1) > 0:
        #         sum += stack1.pop()
        #     if len(stack2) > 0:
        #         sum += stack2.pop()
        #     carry = sum / 10
        #     stack3.append(sum % 10)

        # head = ListNode(0) # set a dumb head
        # tmp = head
        # for i in xrange(len(stack3)-1, -1, -1):
        #     tmp.next = ListNode(stack3[i])
        #     tmp = tmp.next
        # return head.next

        length1, length2 = 0, 0
        cpy1, cpy2 = l1,l2
        # count length
        while cpy1:
            length1 += 1
            cpy1 = cpy1.next
        while cpy2:
            length2 += 1
            cpy2 = cpy2.next
        maxLength = max(length1, length2)

        stack = []
        cpy1, cpy2 = l1,l2
        # append tmp add result
        for i in xrange(maxLength-1, -1, -1):
            sum = 0
            if i+1 <= length1:
                sum += cpy1.val
                cpy1 = cpy1.next
            if i+1 <= length2:
                sum += cpy2.val
                cpy2 = cpy2.next
            stack.append(sum)

        # reconstruct
        carry, l = 0, None
        while stack:
            sum = carry + stack.pop()
            carry = sum // 10
            tmpnode = ListNode(sum%10)
            tmpnode.next = l
            l = tmpnode
        head = l
        if carry > 0:
            head = ListNode(carry)
            head.next = l

        return head




        
