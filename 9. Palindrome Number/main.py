class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if(x<0):
            return False
        
        q=x
        num=0
        while q > 0:
            q,r = divmod(q,10)
            num = num*10 + r

        return num == x;
            
        '''
        i=0
        s = str(x)
        n = len (s)-1
        
        while (i<n):
            if(s[i]!=s[n]):
                return False
            i = i + 1
            n = n - 1
        return True
        '''