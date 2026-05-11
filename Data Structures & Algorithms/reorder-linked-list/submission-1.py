# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def findlast(h, prev = None):
            if h.next is None:
                if prev:
                    prev.next = None
                print('last', h.val, h.next)
                return h
            else: 
                # print('next', h.val)
                return findlast(h.next, h)
        
        a = None
        t = None
        i = 0
        while head is not None:
            if a is None:
                a = head
                t = a
                head = head.next
                # print('init', t.val, head.val)
            else:
                t.next = findlast(head)
                t = t.next
                # print('odds', t.val, head.val, head.next, t.next)
                if t == head:
                    head.next = None
                    # print("same")
                # print('nextt', t.next.val, head.next, t.next)
                else:
                    t.next = head
                t = t.next
                head = head.next
                # print('evens', t.val, head.val, head.next)
            i += 1
            print(i)
        else:
            print('fin')
                
                
        