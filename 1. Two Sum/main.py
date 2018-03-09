class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dct= dict()
        for i,n in enumerate(nums):
            a = str(target-n) 
            if a in dct:
                return [i,dct[a]]
            if str(n) not in dct:
                dct[str(n)] = i