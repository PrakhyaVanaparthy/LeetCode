# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        addedlist = ListNode(0)
        carry = 0
        total = 0
        x = addedlist
        
        while l1 or l2 or carry:
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
                
            total += carry    
            x.next = ListNode(total%10)
            carry = (total//10)
            total =0
            x = x.next
            
        return addedlist.next
