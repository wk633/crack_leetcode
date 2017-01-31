class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        fast = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        
