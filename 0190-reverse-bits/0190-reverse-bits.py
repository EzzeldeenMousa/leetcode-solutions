class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bina = format(n, '032b')
        rev = bina[::-1]

        return int(rev, 2) 
