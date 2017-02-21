# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if len(strs) == 0:
#             return ""
#         result = strs[0]
#
#         for string in strs:
#             while result and string[:len(result)] != result:
#                 result = result[:-1]
#         return result

# a faster version by binary search
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        minlength = min([len(item) for item in strs])
        low, high = 0, minlength
        while low <= high:
            mid = low + (high - low) / 2
            if self.compare(strs, mid):
                low = mid + 1
            else:
                high = mid - 1
        return strs[0][:min(low,high)]

    def compare(self, strs, end):
        target = strs[0][:end]
        for item in strs:
            if item.startswith(target):
                continue
            else:
                return False
        return True
