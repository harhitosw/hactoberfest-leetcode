# https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:  return l2           
        if not l2:  return l1           
        
        head=ListNode(0)                
        cp=head                         
        
        while l1 and l2:                
            
            if l1.val<l2.val:           
                cp.next=l1
                l1=l1.next
            else:                       
                cp.next=l2
                l2=l2.next
                
            cp=cp.next
        if l1:                     
            cp.next=l1
        elif l2:                   
            cp.next=l2
        head=head.next                  
        return head 
