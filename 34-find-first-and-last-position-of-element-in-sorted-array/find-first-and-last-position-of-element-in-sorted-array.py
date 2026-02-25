class Solution(object):
    def searchRange(self, nums, target):
        """
        Time Complexity TC O log n
        Space Complexity SC O 1
        """
        
        def bound(left_search):
            left, right = 0, len(nums) - 1
            ans = -1
            
            while left <= right:
                mid = (left + right)
                
                if nums[mid] == target:
                    ans = mid
                    if left_search:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return ans
        
        return [bound(True), bound(False)]
        