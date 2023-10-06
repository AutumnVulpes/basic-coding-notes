# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Using a single pointer, and doing two passes
# First pass to get length of list
# Note edge case of head itself deleted, just return head.next :D
# Second, go through (length - n - 1) nodes from the start and delete next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0

        while curr:
            curr = curr.next
            length = length + 1

        if length == n: 
            return head.next
        
        curr = head
        for i in range(1, length - n):
            curr = curr.next
        
        curr.next = curr.next.next
        return head