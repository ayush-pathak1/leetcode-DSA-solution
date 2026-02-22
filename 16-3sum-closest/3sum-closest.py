class Solution(object):
    def threeSumClosest(self, nums, target):
        # Time Complexity: O(n^2)
        # - Sorting takes O(n log n)
        # - Outer loop runs O(n)
        # - Inner two-pointer loop runs O(n)
        # - Overall: O(n^2)
        
        # Space Complexity: O(1)
        # - No extra space used (in-place sorting)
        # - Only a few variables are used
        
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total

        return closest