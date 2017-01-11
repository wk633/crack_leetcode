Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])


### 解题思路
f(0) = 1 (除掉0这个特殊数字)
f(1) = 1 + 9 （0 + 1——9中unique number）
f(2) = 1 + 9 + 9*9 （0 + 1-9 + 10 - 99）
f(3) = 1 + 9 + 9*9 + 9*9*8
