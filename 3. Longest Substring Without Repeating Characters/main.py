class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
        '''
        d = dict()
        ll=i=a=0
        lens = len(s)
        
        while (lens-i > ll):
            count = i
            for l in s[i:]:
                if l in d:
                    if a>ll:
                        ll=a
                    a=0
                    i=d[l]+1
                    d = dict()
                    break
                else:
                    d[l]=count
                    count = count + 1
                    a = a + 1
        return ll
        '''         
        