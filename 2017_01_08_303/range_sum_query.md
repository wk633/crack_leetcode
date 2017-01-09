Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
```
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```

Note:
You may assume that the array does not change.
There are many calls to sumRange function.

dp第一题，easy级别

### 累加数列
```
a = [1, 2, 3, 4, 5]
a_acc_sum = [1, 3, 6, 10, 15]

sumRange(2,4) = 12
```
