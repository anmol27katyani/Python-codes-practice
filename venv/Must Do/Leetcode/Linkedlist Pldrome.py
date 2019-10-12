
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if (not head or head.next is None):
            return head
        else:
            curr = head
            last=head
            while(curr.next is not None):
                if(curr.val == curr.next.val):
                    curr = curr.next
                elif  curr.next is not None:
                    last.next = curr.next
                    curr=curr.next
                    last=curr
                    print(curr.val)
            last.next=curr.next
            return head