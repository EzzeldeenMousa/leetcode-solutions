class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        maxi = max(candies)

        for candy in candies:
            if (candy + extraCandies) >= maxi:
                result.append(True)
            else:
                result.append(False)
        return result        