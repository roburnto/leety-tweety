# Last updated: 1/12/2026, 1:41:24 PM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = []
        most = max(candies)
        for candy in candies:
            if candy + extraCandies >= most:
                res.append(True)
            else:
                res.append(False)
        return res