# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 and l2:
            digit = l1.val + l2.val + carry
            if digit >= 10:
                carry = 1
                digit = digit % 10
            else:
                carry = 0
            tail.next = ListNode(val=digit)
            tail = tail.next
            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                digit = l1.val + carry
                if digit >= 10:
                    carry = 1
                    digit = digit % 10
                else:
                    carry = 0
                tail.next = ListNode(val=digit)
                tail = tail.next
                l1 = l1.next
        elif l2:
            while l2:
                digit = l2.val + carry
                if digit >= 10:
                    carry = 1
                    digit = digit % 10
                else:
                    carry = 0
                tail.next = ListNode(val=digit)
                tail = tail.next
                l2 = l2.next
        
        if carry:
            tail.next = ListNode(val=1)
        
        return dummy.next
