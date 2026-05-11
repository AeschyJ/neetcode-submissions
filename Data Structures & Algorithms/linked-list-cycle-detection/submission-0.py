# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        l = len(s)
        while head is not None:
            s.add(head)
            if l == len(s): return True
            else:
                l = len(s)
            head = head.next
        else:
            return False
        