"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head: return None
        
        map = {}
        temp = head
        while temp:
            map[temp] = Node(temp.val)
            temp = temp.next
        
        curr = head
        while curr:
            if curr.next:
                map[curr].next = map[curr.next]
            if curr.random:
                map[curr].random = map[curr.random]
            curr = curr.next
        
        return map[head]
