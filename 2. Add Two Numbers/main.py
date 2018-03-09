# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c=0;
        rn = tn = None
        while(l1 is not None and l2 is not None):
            n1 = l1.val
            n2 = l2.val
            x = n1 + n2 + c
            if (x>=10):
                c=1
                x=x-10
            else:
                c=0
            
            if(rn is None):
                tn = rn = ListNode(x)
            else:
                tn.next = ListNode(x)
                tn = tn.next;
                      
            l1 = l1.next;
            l2 = l2.next;
            if(l1 is None and l2 is None):
                if(c==1):
                    tn.next = ListNode(1)
                    tn = tn.next;
                return rn
            
        if(l1 is None):
            while(l2 is not None or c==1):
                if(l2 is None):
                    b=c
                else:
                    b = c + l2.val
                    l2 = l2.next;
                n2 = b
                
                if (n2>=10):
                    c=1
                    n2=n2-10
                else:
                    c=0
                tn.next = ListNode(n2)
                tn = tn.next;
                
        elif(l2 is None):
            while(l1 is not None or c==1):
                if(l1 is None):
                    b=c
                else:
                    b = c + l1.val
                    l1 = l1.next;
                n1 = b
                
                if (n1>=10):
                    c=1
                    n1=n1-10
                else:
                    c=0
                tn.next = ListNode(n1)
                tn = tn.next;
                
        return rn