class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n+1)               

        for i in range(len(ans)):
            ans[i] = format(i, 'b').count('1')
        return ans

        