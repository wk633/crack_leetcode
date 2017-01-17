def decode(s):
    rst = [["",1]]
    num = ""
    for item in s:
        if item.isdigit():
            num += item
        elif item == "[":
            rst.append(["",int(num)])
            num = ""
        elif item == "]":
            rst[-2][0] += rst[-1][0]*rst[-1][1]
            rst.pop()
        else:
            rst[-1][0] += item
    return rst[0][0]
print decode('3[a]2[bc]')
print decode("3[a2[c]]")
print decode("2[abc]3[cd]ef")
