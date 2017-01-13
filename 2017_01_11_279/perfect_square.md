Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

### 思路
n为0时，为0
n为1时，为1
n>=2, 开始计算完全平方数最大到哪，得到一个lst
每轮用一个集合来记录每轮分配情况，即还剩多少数字
