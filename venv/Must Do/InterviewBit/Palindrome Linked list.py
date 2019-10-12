#Approach 1: Simple iterative using stacks
#Approach 2: Simple using half reverse and iteratively traversing
#Approach 3: Recursively
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
class Solution:
    def lPalin(self, head):
        if not head or not head.next:
            return 1
        self.current = head

        return self.compare(head)

    def compare(self, head):
        if not head: return 1
        if not self.compare(head.next): return 0

        if head.val != self.current.val:
            return 0
        else:
            self.current = self.current.next
            return 1
    # @param A : head node of linked list
    # @return an integer