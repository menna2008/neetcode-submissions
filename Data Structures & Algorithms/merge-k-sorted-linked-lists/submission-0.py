# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        merged = 0
        dummy = ListNode()
        tail = dummy

        while True:
            mini = -1
            for i in range(k):
                if not lists[i]: continue
                if mini == -1 or lists[i].val < lists[mini].val:
                    mini = i
            
            if mini == -1: break

            tail.next = lists[mini]
            lists[mini] = lists[mini].next
            tail = tail.next
        
        return dummy.next
        