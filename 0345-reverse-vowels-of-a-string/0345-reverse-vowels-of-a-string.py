class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        l = 0
        r = len(s) - 1
        stri = list(s)

        while l < r:
            if stri[l] not in vow:
                l += 1
            elif stri[r] not in vow:
                r -= 1
            else:
                stri[l], stri[r] = stri[r], stri[l]
                l += 1
                r -= 1
        return "".join(stri)
        