# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        iters = length // k
        curr = head
        prev_tail = None

        for it in range(iters):
            start = curr
            prev = curr
            curr = curr.next
            for i in range(k - 1): 
                nx = curr.next
                curr.next = prev
                prev = curr
                curr = nx

            if prev_tail:
                prev_tail.next = prev
            else:
                head = prev

            start.next = curr
            prev_tail = start
        
        return head
