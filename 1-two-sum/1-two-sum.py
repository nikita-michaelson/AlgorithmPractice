class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ## enumerate allows for an output of index then value
        for i, num in enumerate(nums):
            ## range produces numbers in sequence, index i+1 then stop at nums length
            for j in range(i + 1, len(nums)):  
                if num + nums[j] == target:
                    return [i, j]