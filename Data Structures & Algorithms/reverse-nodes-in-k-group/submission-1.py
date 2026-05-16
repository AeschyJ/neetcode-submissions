# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        curr = dummy
        while head:
            arr = []
            for i in range(k):
                if head:
                    arr.append(head)
                    head = head.next
                else:
                    break
            if len(arr) == k:
                for i in range(len(arr) - 1, 0, -1):
                    print(arr[i].val, arr[i-1].val, arr[i].next)
                    arr[i-1].next = None
                    arr[i].next = arr[i-1]
                curr.next = arr[-1]
                curr = arr[0]
            else:
                curr.next = arr[0]
        return dummy.next
                
                