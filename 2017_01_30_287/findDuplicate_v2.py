class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = nums[0]
        slow = nums[slow]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
