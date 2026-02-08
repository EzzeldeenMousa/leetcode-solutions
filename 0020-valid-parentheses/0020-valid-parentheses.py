class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {')':'(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            if char not in d:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if stack.pop() != d[char]:
                        return False
                    
        
        return not stack
                    
                

                
                
                    