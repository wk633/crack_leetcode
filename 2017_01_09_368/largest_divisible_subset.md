理解了一个python版本的解答

```python
def largestDivisibleSubset(self, nums):
    S = {-1: set()}
    for x in sorted(nums):
        S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
    return list(max(S.values(), key=len))
```



链接： https://discuss.leetcode.com/topic/49455/4-lines-in-python



关键点是如果 x 能整除某个满足条件（是一个largest divisible subset）的集合中最大的那个数，那么向这个集合中添加x形成的新集合也是一个largest divisible subset。

其他就是python中max的用法，key参数收比较用的函数，len是内置的长度函数

比如`max(([2,3,4,5], [3,4,5], [4,5]), key=len)` 功能就是返回最长的数组

另外`|`可以对集合进行“或”操作

`{x}`含义是`set(x)`

