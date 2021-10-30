class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 1
        while end <= len(s):
            if len(set(s[start:end])) != len(s[start:end]):
                start += 1
                end += 1
            else:
                end += 1
        return end - start - 1