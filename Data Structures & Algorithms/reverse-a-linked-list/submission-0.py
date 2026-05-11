# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = None
        head = ListNode(head) if type(head) is not ListNode else head
        while head.next is not None:
            if a is None:
                # print("init", a, head.val, head.next)
                a = ListNode(head.val)
                head = head.next
            else:
                # print("loop", a.val, head.val, head.next)
                t = a
                a = ListNode(head.val, t)
                head = head.next
        else:
            # print("final", head.val, head.next)
            t = a
            a = ListNode(head.val, t)
        return a if a.val is not None else ListNode('')
            