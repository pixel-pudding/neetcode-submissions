# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #if the slow pointer catches upto the fast then cycle existis
        slow=head #intialise the slow pointer 
        fast=head #Intialise the fast pointer 
        while(fast!=None and fast.next!=None):
            slow=slow.next #move slow pointer by one node 
            fast=fast.next.next #move fast pointer by two nodes 
            if(slow==fast):
                return True #slow pointer catches to fast pointer therefore there is a cylce
        return False
        