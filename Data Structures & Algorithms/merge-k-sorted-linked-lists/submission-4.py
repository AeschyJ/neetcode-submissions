# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergetwo(list1, list2):
            head = ListNode(None,None)
            curr = head
            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    curr, list1 = curr.next, list1.next
                else:
                    curr.next = list2
                    curr, list2 = curr.next, list2.next
            curr.next = list1 or list2
            return head.next
        
        l = len(lists)
        interval = 1
        while interval < l:
            for i in range(0, l - interval, interval * 2):
                lists[i] = mergetwo(lists[i], lists[i+interval])
            interval *= 2
        if lists and lists[0]:
            return lists[0]
        return
        