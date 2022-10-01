
# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        k = 0
        s = (l1.val + l2.val + k)
        if(s >= 10):
            s = s % 10
            k = 1
        else:
            k = 0
        l3 = ListNode(s)
        start = l3

        while(l1.next != None and l2.next != None):
            l1 = l1.next
            l2 = l2.next
            s = (l1.val + l2.val + k)
            if(s >= 10):
                s = s % 10
                k = 1
            else:
                k = 0
            node = ListNode(s)
            l3.next = node
            l3 = l3.next

        while(l1.next != None):
            l1 = l1.next
            s = (l1.val + k)
            if(s >= 10):
                s = s % 10
                k = 1
            else:
                k = 0
            # print(l3.val,k,s)
            node = ListNode(s)
            l3.next = node
            l3 = l3.next

        while(l2.next != None):
            l2 = l2.next

            s = (l2.val + k)
            if(s >= 10):
                s = s % 10
                k = 1
            else:
                k = 0
            node = ListNode(s)
            l3.next = node
            l3 = l3.next

        if(k != 0):
            node = ListNode(k)
            l3.next = node
            l3 = l3.next

        print(start, l3)
        return start
