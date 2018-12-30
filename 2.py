# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def OneDigit(self,bit1,bit2,carry_in,result):
        if bit1==None:
            if bit2==None:
                return
            else:
                Sum=bit2.val+carry_in
                if Sum-10>=0:
                    result.val=Sum-10
                    result.next=ListNode(0)
                    if bit2.next!=None:

                        self.OneDigit(None,bit2.next,1,result.next)
                    else:
                        result.next.val=1
                else:
                    result.val=Sum
                    if bit2.next!=None:
                        result.next=ListNode(0)
                        self.OneDigit(None,bit2.next,0,result.next)
        else:
            if bit2==None:
                Sum=bit1.val+carry_in
                if Sum-10>=0:
                    result.val=Sum-10
                    result.next=ListNode(0)
                    if bit1.next!=None:
                        
                        self.OneDigit(bit1.next,None,1,result.next)
                    else:
                        result.next.val=1
                else:
                    result.val=Sum
                    if bit1.next!=None:
                        result.next=ListNode(0)
                        self.OneDigit(bit1.next,None,0,result.next)
            else:
                Sum=bit1.val+bit2.val+carry_in
                if Sum-10>=0:
                    result.val=Sum-10
                    result.next=ListNode(0)
                    if not (bit1.next==None and bit2.next==None):
                        self.OneDigit(bit1.next,bit2.next,1,result.next)
                    else:
                        result.next.val=1
                else:
                    result.val=Sum
                    if not (bit1.next==None and bit2.next==None):
                        result.next=ListNode(0)
                        self.OneDigit(bit1.next,bit2.next,0,result.next)
    def addTwoNumbers(self, l1, l2):
        result =ListNode(0)
        self.OneDigit(l1,l2,0,result)
        return result
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
