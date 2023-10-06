# https://leetcode.com/problems/reverse-linked-list/
# B constraint: Using stack (append and pop)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1: Iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            next = curr.next  # Marking next node
            curr.next = prev  # Reverse current node's pointer
            
            # Move all the pointers forward by 1
            prev = curr
            curr = next
        return curr
    
# Solution 2: Stack
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []
        if not head:
            return None

        while head:
            stack.append(head)
            head = head.next

        init = stack.pop()
        curr = init

        while stack:
            curr.next = stack.pop()
            curr = curr.next
        curr.next = None

        return init