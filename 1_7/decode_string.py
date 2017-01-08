# -*- coding:utf-8 -*-

def decodeString(s):
    num = "" # 多位数字需要字符串拼接
    stack = [["",1]]
    for ch in s:
        if ch.isdigit():
            print 'digit case'
            num += ch
        elif ch == '[':
            print '"[" case'
            stack.append(["",int(num)])
            num = ""
        elif ch == ']':
            print '"]" case'
            st, k = stack.pop()
            stack[-1][0] += k*st
        else:
            print 'other case: ', ch
            stack[-1][0] += ch
        print stack,"\n"
    return stack[-1][0]


decodeString('3[a2[c]]')
# decodeString('2[abc]3[cd]ef')
