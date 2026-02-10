class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""

        for i in range(len(strs[0])):
            for char in strs:
                if i == len(char) or char[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        
        return result
        
       