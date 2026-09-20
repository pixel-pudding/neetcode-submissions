# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head 
        prev=None
        while(current!=None):
            nextnode=current.next #save the next node 
            current.next=prev #reverse the link
            prev=current #Move prev forward 
            current=nextnode #move current forward 
        return prev #new head is given by prev
        