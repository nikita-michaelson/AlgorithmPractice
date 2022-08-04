class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # create an hashmap with a list as the key and count as the value 
        result = defaultdict(list) # avoid problem if count dne 
        
        for stri in strs:
            count = [0] * 26 #list of 26 indices represnting the letters a - z
        
            for letters in stri: 
                count[ord(letters) - ord("a")] +=1 # a-a = 0, z-a = 25
                
            result[tuple(count)].append(stri) # add list of strings as values to the keys, letter counts
        
        return result.values()