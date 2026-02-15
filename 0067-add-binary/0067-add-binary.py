class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digita = a[i] if i < len(a) else 0
            digitb = b[i] if i < len(b) else 0
 
            total = int(digita) + int(digitb) + carry
            char = str(total % 2)
            res += char
            carry = total // 2
        if carry:
            res += "1"
        return res[::-1]
               

        