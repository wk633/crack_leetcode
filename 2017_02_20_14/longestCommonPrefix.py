class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        result = strs[0]

        for string in strs:
            while result and string[:len(result)] != result:
                result = result[:-1]
        return result
