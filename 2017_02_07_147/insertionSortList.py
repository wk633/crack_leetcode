# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        dummy = ListNode(None) # dummy head, use .next to access the linked list node
        while head:
            node = dummy
            while node.next and head.val > node.next.val:
                node = node.next
            tmpnode = node.next            # store the insertion start node
            node.next = ListNode(head.val) # create new node
            node.next.next = tmpnode       # connect two linked list
            head = head.next               # head go on
        return dummy.next


        
