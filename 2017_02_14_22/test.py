def gen(n):
    def dfs(s, left, right, rst):
        if left:
            dfs(s+"(", left-1, right, rst)
        if right > left:
            dfs(s+")", left, right-1, rst)
        if not right:
            rst.append(s)
        return rst
    return dfs("", n, n, [])
print gen(3)
