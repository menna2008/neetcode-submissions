# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = group_prev
            i = 0
            while i < k and kth:
                kth = kth.next
                i += 1
            
            if not kth: break
            
            group_next = kth.next
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                nx = curr.next
                curr.next = prev
                prev = curr
                curr = nx
            
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
        
        return dummy.next
