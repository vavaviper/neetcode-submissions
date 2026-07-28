# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == [] and list2 == []:
            return []
        if not list1:
            return list2
        if not list2:
            return list1
        final = None
        if list1.val <= list2.val:
            start = list1
            list1 = list1.next
        else:
            start = list2
            list2 = list2.next
        final = start
        while list1 and list2:
            if list1.val <= list2.val:
                final.next = list1
                list1 = list1.next
            else:
                final.next = list2
                list2 = list2.next
            final = final.next
        if list1:
            final.next = list1
        else:
            final.next = list2
        return start

            
