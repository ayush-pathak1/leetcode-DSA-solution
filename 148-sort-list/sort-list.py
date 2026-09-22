class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Base case
        if not head or not head.next:
            return head
        
        # 1. Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Split the list into two halves
        mid = slow.next
        slow.next = None
        
        # 2. Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # 3. Merge two sorted lists
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
            
        return dummy.next