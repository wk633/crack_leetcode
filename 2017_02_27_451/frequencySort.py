class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join(c*freq for c,freq in collections.Counter(s).most_common())
