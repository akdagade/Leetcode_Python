"""
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
"""

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