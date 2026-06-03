# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        temp = head
        while temp:
            sz += 1
            temp = temp.next
        
        remove = sz - n
        if remove == 0: return head.next

        cur = head
        for i in range(sz - 1):
            if (i + 1) == remove:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
        