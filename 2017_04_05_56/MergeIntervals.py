# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        result = []
        for item in sorted(intervals, key=lambda x: x.start):
            if result and result[-1].end >= item.start:
                result[-1].end = max(item.end, result[-1].end)
            else:
                result.append(item)
        return result
