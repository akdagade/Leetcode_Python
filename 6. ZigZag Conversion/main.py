class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows==1):
            return s
        
        ns=''
        for i in range(numRows):
            c=0
            l=0
            while l<len(s):
                if(i==0):
                    ns = ns + s[l]
                    c = c + 1
                    l = 2*c*(numRows-1)
                    #print('1')

                elif(i==numRows-1):
                    l = (2*c+1)*(numRows-1)
                    c = c + 1
                    if(l>=len(s)):
                        break
                    ns = ns + s[l]
                    #print('2')

                else:
                    l = 2*c*(numRows-1) + i 
                    if(l>=len(s)):
                        break
                    ns = ns + s[l]
                    c = c + 1
                    l = 2*c*(numRows-1) - i 
                    if(l>=len(s)):
                        break
                    ns = ns + s[l]

        return ns
        
        """
        #s="PAYPALISHIRING"
        #numRows=3
        if(numRows==1):
            return s
        
        col = numRows * (int(len(s)/(2*numRows -1))+1)
        mat = [['' for j in range(col)] for i in range(numRows)] 
            
        i=j=0;
        
        for l in s:
            mat[i][j]=l
            if(j%(numRows-1)==0 and i+1<numRows):
                i=i+1
            else:
                i=i-1
                j=j+1
                
        s=''
        for i in range(numRows):
            for j in mat[i]:
                s = s + j
                
        return s
        """