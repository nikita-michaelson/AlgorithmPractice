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

        #two hashmap approach
        #key = the letter, value = the number of occurences 
        countS, countT = {}, {}
        
        for i in range(len(s)):
            #make the key the letter and value the count , get returns the value
            
            countS[s[i]] = 1 + countS.get(s[i],0) 
            countT[t[i]] = 1 + countT.get(t[i],0) 
            
        return countS == countT
    
    #--------------------------------------------------------------------
    
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