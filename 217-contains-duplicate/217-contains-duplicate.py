class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    ## utilize set which has no values , only keys 
        check = set()
        for num in nums:
            if num in check:
                return True
            else:
                check.add(num)
        else:
            return False
   