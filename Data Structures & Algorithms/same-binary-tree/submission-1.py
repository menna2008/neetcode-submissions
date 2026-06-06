# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False

        stack_p, stack_q = [p], [q]
        while stack_p and stack_q:
            curr_p, curr_q = stack_p.pop(), stack_q.pop()
            if not curr_p and not curr_q: continue
            if not curr_p or not curr_q or curr_p.val != curr_q.val:
                return False
            stack_p.append(curr_p.left)
            stack_p.append(curr_p.right)
            stack_q.append(curr_q.left)
            stack_q.append(curr_q.right)
        
        return len(stack_p) == len(stack_q)
        