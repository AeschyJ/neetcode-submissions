# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = None
        t = None
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                if a is None: 
                    a = list1
                if t is None:
                    t = a
                else:
                    t.next = list1
                    t = t.next
                list1 = list1.next
            else:
                if a is None: 
                    a = list2
                if t is None: 
                    t = a
                else:
                    t.next = list2
                    t = t.next
                list2 = list2.next
        else:
            if list1 is not None:
                if a is None: a = list1
                else: t.next = list1
            elif list2 is not None:
                if a is None: a = list2
                else: t.next = list2
        return a if a is not None else ListNode('')
                
        