class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """  
        hashmap = {}
        for index,value in enumerate(nums):
            #value as the key so we can utilize the has_key method
            diff = target - value
             
            if diff in hashmap:
                return [hashmap[diff], index]
            hashmap[value] = index
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # ## enumerate allows for an output of index then value
        # for i, num in enumerate(nums):
        #     ## range produces numbers in sequence, index i+1 then stop at nums length
        #     for j in range(i + 1, len(nums)):  
        #         if num + nums[j] == target:
        #             return [i, j]