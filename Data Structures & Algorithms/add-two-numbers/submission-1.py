# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a, curr, prev = None, None, None
        while l1 is not None or l2 is not None:
            total = 0 if not curr else curr.val
            if l1 is not None:
                total += l1.val
            if l2 is not None:
                total += l2.val
            if total >= 10:
                if not curr:
                    curr = ListNode(total % 10, ListNode(total // 10))
                    a = curr
                    prev = curr
                    curr = curr.next
                else:
                    curr.val = total % 10
                    curr.next = ListNode(total // 10)
                    curr = curr.next
                    prev = prev.next
            else:
                if not curr:
                    curr = ListNode(total, ListNode())
                    a = curr
                    prev = curr
                    curr = curr.next
                else:
                    curr.val = total
                    curr.next = ListNode()
                    curr = curr.next
                    prev = prev.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if curr and curr.val == 0:
            prev.next = None
        if a: return a
        return