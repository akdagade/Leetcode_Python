class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        r=x;
        if n==0:
            return 1
        elif n>0:
            for  i in range(n-1):
                r = r*x
        else:
            for  i in range((-1*n)-1):
                r = r*x
            r = 1/r
        return r