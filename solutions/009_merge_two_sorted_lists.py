# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
            self,
            list1: Optional[ListNode],
            list2: Optional[ListNode]) -> Optional[ListNode]:

        res = sorted_list = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                sorted_list.next = list1
                list1 = list1.next
            else:
                sorted_list.next = list2
                list2 = list2.next
            sorted_list = sorted_list.next
        
        sorted_list.next = list1 if list1 else list2
        return res.next
    
# Create queue
# Instead of linked nods, populate deque
# Return queue