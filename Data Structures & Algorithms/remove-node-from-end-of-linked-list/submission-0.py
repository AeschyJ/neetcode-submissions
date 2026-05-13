# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 1
        a = head
        re = None
        reprev = None
        while head:
            if not re:
                re = head
            if i > n:
                reprev, re = re, re.next
                i -= 1
                # print(head.val, reprev.val, re.val, i)
            head = head.next
            i += 1
        if not reprev:
            a = re.next
            if not a: a = ListNode('')
        else:
            reprev.next = re.next
        return a
            
            
        