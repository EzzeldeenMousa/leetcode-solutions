class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bina = bin(n)[2:]

        for i in range(len(bina)-1):
            if bina[i] == bina[i+1]:
                return False
            else: continue
        return True        