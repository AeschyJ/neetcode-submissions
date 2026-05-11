# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        f, s = head, head
        while f and f.next:
            f, s = f.next.next, s.next
        
        prev, curr = None, s.next
        s.next = None
        while curr:
            n = curr.next
            curr.next = prev
            prev, curr = curr, n

        h1, h2 = head, prev
        while h2:
            t1, t2 = h1.next, h2.next
            h1.next, h2.next = h2, t1

            h1, h2 = t1, t2

        
        