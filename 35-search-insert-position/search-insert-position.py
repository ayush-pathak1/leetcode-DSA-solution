class Solution(object):
    def searchInsert(self, nums, target):
        """
        Time Complexity (TC): O(log n)
         Binary search halves the search space each iteration
         
        Space Complexity (SC): O(1)
         No extra space used (constant space)
        """
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left