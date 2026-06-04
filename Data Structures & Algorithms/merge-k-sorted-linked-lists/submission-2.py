# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None

        heap = []
        for ls in lists:
            if ls:
                heapq.heappush(heap, NodeWrapper(ls))
        
        dummy = ListNode()
        tail = dummy
        while heap:
            wrapper = heapq.heappop(heap)
            tail.next = wrapper.node
            tail = tail.next
            if wrapper.node.next:
                heapq.heappush(heap, NodeWrapper(wrapper.node.next))
        
        return dummy.next
        