/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 *     https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
 * };
 */
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        //base condition if only one node exsist
        if(!head->next) return nullptr;
        ListNode *tmp=head;
        int mid=1;
        // find the centre Node of Linked List
        while(tmp->next){
            mid++;
            tmp=tmp->next;
        }
        // we need to take the ceil of Mid iff the number of Nodes in List is even 
        mid=(mid)/2;
        mid=mid-1;
        tmp=head;
        //stop at the middle of the Linked List 
        while(mid>0){
            tmp=tmp->next;
            mid--;
        }
        // disconnect the node and you are Done 
        tmp->next=tmp->next->next;
        return head;
        
    }
};