class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        l1 = 0
        l2 = 0

        while l1 < len(word1) and l2 < len(word2):
            result.append(word1[l1])
            result.append(word2[l2])
            l1+=1
            l2+=1
        if l1 < len(word1):
            result.append(word1[l1:])
        if l2 < len(word2):
            result.append(word2[l2:])
        return "".join(result)        
            
        


        
        