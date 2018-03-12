class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = len(nums)
        f = 0
        n=val
        if l==1 and nums[0]==n:
            del nums[0]
            return 0
        
        if l==0:
            return 0

        while f<l-1:
            front = nums[f]
            last =  nums[l-1]

            if front==n and last!=n:
                nums[f] = last
                f = f+1
                l = l-1

            elif (last==n):
                l = l-1

            elif front!=n and last!=n:
                f = f+1	

        if(nums[l-1]==n):
            l=l-1
            
        
        return l