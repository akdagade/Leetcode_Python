class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        for l in s:
            if l in ['{','(','[']:
                stack.append(l)
                #print(stack)
            elif l in ['}',')',']']:
                if(len(stack)<=0):
                    return False
                c = stack.pop()
                if ((l=='}' and c !='{') or (l==')' and c !='(') or (l==']' and c !='[')):
                    return False
        
        if(len(stack)>0):
            return False
        return True