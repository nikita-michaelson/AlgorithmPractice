class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        #first check if same length 
        if len(s) != len(t):
            return False
        
        #sort both strings, if they are anagrams, they will be the same
        
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else:
            return False