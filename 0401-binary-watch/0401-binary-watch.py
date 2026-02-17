class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        res = []
        if turnedOn > 8: return []

        for h in range(12):
            for m in range(60):
                if turnedOn == (bin(h).count('1') + bin(m).count('1')):
                    res.append("{}:{:02d}".format(h, m))

        return res

               
        