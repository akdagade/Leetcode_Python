# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nd = []
        t = head
        ln=0
        while t is not None:
            nd.append(t)
            ln = ln + 1
            t = t.next
        
        if (ln == 1 and n==1):
            return None
        ln = ln - n
  
        if(ln==0):
            head=nd[ln+1]
            return head
        
        nd[ln-1].next = nd[ln].next     
        return head