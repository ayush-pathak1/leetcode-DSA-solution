# Problem: Two Sum
# Pattern: Sorting + Two Pointers
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums, target):
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()
        
        left = 0
        right = len(arr) - 1
        
        while left < right:
            total = arr[left][0] + arr[right][0]
            
            if total == target:
                return [arr[left][1], arr[right][1]]
            elif total < target:
                left += 1
            else:
                right -= 1