class Solution(object):
    def containsDuplicate(self, nums):
        """
        Time Complexity TC O n
        Space Complexity SC O n
        """
        return len(nums) != len(set(nums))