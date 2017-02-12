Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

Subscribe to see which companies asked this question.

### Solution
first iterate linked list to get the total length and get the tail node,
then connect tail and head
finally find the node before "result head node", change it next value
