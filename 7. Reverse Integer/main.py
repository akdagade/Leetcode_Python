class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        
        if(x<0):
            s = s[1:]
            s = int('-' + s[::-1])
            if (s < -2147483648) :
                return 0
            return s
        
        if (int(s[::-1]) > 2147483648):
            return 0
        return (int(s[::-1]))