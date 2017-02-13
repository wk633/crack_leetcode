Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

### solution
first create a dummy node

then iterate:
preNode --> curNode --> nextNode --> nextNode.next
preNode --> nextNode --> curNode --> nextNode.next

iteration end condition is preNode.next and preNode.next.next all exist
