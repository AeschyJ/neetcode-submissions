# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        head = ListNode(None,None)
        curr = head
        h = []
        for i, j in enumerate(lists):
            if j:
                heapq.heappush(h, (j.val, i, j))
        if h: print(h)
        while h:
            val, i, j = heapq.heappop(h)
            curr.next = j
            curr = curr.next
            if j.next:
                heapq.heappush(h, (j.next.val, i, j.next))
        return head.next
        