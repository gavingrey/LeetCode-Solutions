class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append('openparen')
            if char == '[':
                stack.append('openbrack')
            if char == '{':
                stack.append('opencurly')
            if not stack:
                return False
            if char == ')':
                top_char = stack.pop()
                if top_char != 'openparen':
                    return False
            if char == ']':
                top_char = stack.pop()
                if top_char != 'openbrack':
                    return False
            if char == '}':
                top_char = stack.pop()
                if top_char != 'opencurly':
                    return False
        return not stack
    
if __name__ == '__main__':
    test = Solution()
    assert test.isValid('()')
    assert test.isValid('()[]{}')
    assert not test.isValid('(]')
    assert not test.isValid('([)]')
    assert test.isValid('{[]}')