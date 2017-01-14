Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

### 思路
https://discuss.leetcode.com/topic/8109/simple-dp-solution-in-python-with-description

### 一些陷阱
```python
>>> a
'abcdefg'
>>> a[1:3]
'bc'
>>> a[3]
'd'
```
因此要记录结尾在[3]，长度为2的子字符串，那么需要访问的是
```
a[3-2+1:3+1] = a[2:4]
```
