# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def checklen(head, k):
            curr = head
            for i in range(k-1):
                if not curr.next:
                    return False
                curr = curr.next
            return True
        dummy = ListNode(None)
        curr = head
        last = dummy
        x = dummy
        while head:
            if checklen(head, k):
                prev = None
                for i in range(k):
                    if i == 0: x, last = head, x
                    head = head.next
                    curr.next = prev
                    prev, curr = curr, head
                # if head.next: print(head.next.val)
                if not dummy.next: dummy.next = prev
                last.next = prev
            else:
                x.next = head
                while head:
                    head = head.next
        return dummy.next