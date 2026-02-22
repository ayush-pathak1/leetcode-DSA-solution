class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Time Complexity: O(n)
        # - We traverse the list once using two pointers.
        
        # Space Complexity: O(1)
        # - Only a few extra pointers are used.
        
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummy.next