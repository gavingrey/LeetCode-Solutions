class Solution:
    
    def charMatch(self, str_char: str, reg_char: str):
        return reg_char == '.' or str_char == reg_char
    
    def isMatch(self, s: str, p: str) -> bool:
        star = (p[1:2] == '*')
        if not s:
            return True if not p else (False if not star else self.isMatch(s, p[2:]))
        if not p:
            return False
        if self.charMatch(s[0], p[0]):
            if star:
                if self.isMatch(s[1:], p):
                    return True
                else:
                    return self.isMatch(s, p[2:])
            else:
                return self.isMatch(s[1:], p[1:])
        else:
            return self.isMatch(s, p[2:]) if star else False
        

if __name__ == '__main__':
    test = Solution()
    assert test.isMatch("aa", "a*")
    assert not test.isMatch("aa", "a")
    assert test.isMatch("ab", ".*")
    assert test.isMatch("aab", "c*a*b")
    assert not test.isMatch("mississippi", "mis*is*p*.")
    assert test.isMatch("mississippi", "mis*is*ip*.")
    assert not test.isMatch("ab", ".*c")
    assert test.isMatch("aaa", "a*a")