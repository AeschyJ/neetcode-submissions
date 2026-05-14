# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while l1 is not None:
            arr.append(f'{l1.val}')
            l1 = l1.next
        arr.reverse()
        i = int("".join(arr))
        arr.clear()
        while l2 is not None:
            arr.append(f'{l2.val}')
            l2 = l2.next
        arr.reverse()
        j = int("".join(arr))
        x = i + j
        a, prev= None, None
        for i, c in enumerate(f"{x}"[::-1]):
            curr = ListNode(int(c))
            if i > 0:
                prev.next = curr
                prev = prev.next
            else:
                prev = curr
                a = prev
        if a:
            return a
        return
        
            