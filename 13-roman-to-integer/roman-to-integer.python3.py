class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        """
        m = {"IV": 4, "IX":9, "XL":40 ,"XC": 90, "CD": 400, "CM":900}
        t = {"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        res = 0
        while s:
            if s[:2] in m:
                res += m[s[:2]]
                s = s[2:]
            else:
                res += t[s[0]]
                s = s[1:]
        return res
        