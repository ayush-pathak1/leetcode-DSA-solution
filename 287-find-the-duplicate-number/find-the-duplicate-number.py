# Time Complexity  : O(n log n)
# Space Complexity : O(1)

class Solution:
    def findDuplicate(self, nums):
        low = 1
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            count = 0

            for n in nums:
                if n <= mid:
                    count += 1

            if count > mid:
                high = mid
            else:
                low = mid + 1

        return low