class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        op = 0

        while any(n > 0 for n in nums):
            x = min(n for n in nums if n > 0)

            nums = [n - x if n > 0 else 0 for n in nums]

            op += 1
        return op  

            
