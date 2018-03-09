class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        l = len(nums)
        if l==0 or l==1:
            return l
        
        dup = nums[0]
        di=1
        for i in range(l):
            if(nums[i]!=dup):
                dup=nums[i]
                nums[di]=dup
                di = di + 1
        if l!=di:
            del nums[-(l-di):]
        print (len(nums))
        