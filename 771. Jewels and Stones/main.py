class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        n=0;
        for i in J:
            for s in S:
                if i==s:
                    n=n+1
        return n