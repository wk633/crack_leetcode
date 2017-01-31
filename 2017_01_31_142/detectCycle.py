class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while True:
            if fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    break
            else:
                return None
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return fast
