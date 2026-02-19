class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_numbers = set(nums)

        if 0 in unique_numbers:
            unique_numbers.remove(0)
        return len(unique_numbers)  

            
