def is_palindrome(s: str):
    return s == s[::-1]

def first_recur(s: str, start: int, end: int, best_recur: str):
    if is_palindrome(s[start:end]) and start > 0 and end < len(s) and is_palindrome(s[start - 1: end + 1]):
        return first_recur(s, start - 1, end + 1, s[start-1:end+1])
    elif end < len(s) and is_palindrome(s[start: end + 1]):
        return first_recur(s, start, end + 1, s[start: end + 1])
    elif start > 0 and is_palindrome(s[start - 1: end]):
        return first_recur(s, start - 1, end, s[start - 1: end])
    elif end < len(s):
        return first_recur(s, start + 1, end + 1, best_recur)
    else:
        return best_recur
            
class Solution:
    def longestPalindrome(self, s: str) -> str:
        return first_recur(s, 0, 1, s[0])