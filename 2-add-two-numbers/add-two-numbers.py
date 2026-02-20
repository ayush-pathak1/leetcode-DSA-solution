# Problem: Add Two Numbers
# Pattern: Linked List + Simulation
# Time Complexity: O(max(n, m))
# Space Complexity: O(max(n, m))

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            tail.next = ListNode(carry % 10)
            tail = tail.next
            carry //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next