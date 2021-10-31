class Solution:
    def myAtoi(self, s: str) -> int:
        allowed = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        s = s.strip()
        substr = ""
        neg = 1
        if s:
            if s[0] == '-':
                s = s[1:]
                neg = -1
            elif s[0] == '+':
                s = s[1:]
        else:
            return 0
        for char in s:
            if char in allowed:
                substr += char
            else:
                break
        return(neg * min(2147483647 + (0 if neg == 1 else 1), abs(int(substr))) if substr else 0)