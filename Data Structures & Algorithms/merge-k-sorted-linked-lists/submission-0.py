# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(None, None)
        curr = head
        d = {}
        for i in range(len(lists)):
            d[i] = lists[i].val
        while any(lists):
            i = min(d, key = d.get)
            if d[i] == math.inf: break
            curr.next = lists[i]
            curr, lists[i] = curr.next, lists[i].next
            d[i] = lists[i].val if lists[i] else math.inf
        return head.next
        