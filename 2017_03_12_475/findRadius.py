class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters) + [float("inf")]
        i, r = 0, 0
        for house in sorted(houses):
            # find the nearest heater
            while heaters[i+1] - house <= house - heaters[i]:
                i += 1
            r = max(r, abs(house - heaters[i]))
            # abs() is to solve the case when the first heater is too far away, so could not find a heater in front of this house
            # e.g. houses: [1,5] heaters: [10]
        return r
# reference:
# points out the key to solve this problem: https://discuss.leetcode.com/topic/71450/simple-java-solution-with-2-pointers
# provide good code: https://discuss.leetcode.com/topic/71456/short-python
