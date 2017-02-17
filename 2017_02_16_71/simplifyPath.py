class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for dir in path.split("/"):
            if dir == ".." and stack:
                stack.pop()
            elif dir != "." and dir != ".." and dir:
                stack.append(dir)
        return "/"+"/".join(stack)



        # stack = [];
        # for dir in path.split("/"):
        #     if dir == "..":
        #         if stack:
        #             stack.pop()
        #     elif dir and dir!=".":
        #             stack.append(dir)
        # return "/"+"/".join(stack)
