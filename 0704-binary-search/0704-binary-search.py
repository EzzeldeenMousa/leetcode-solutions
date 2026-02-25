class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0

        for i in range(len(nums)):
            if target not in nums:
                return -1
            elif nums[i] != target:
                i += 1
            else:
                return i