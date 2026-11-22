"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        oldtonew = {}
        curr = head
        while curr:
            oldtonew[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            oldtonew[curr].next = oldtonew.get(curr.next)
            oldtonew[curr].random = oldtonew.get(curr.random)
            curr = curr.next
        return oldtonew[head]