class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        min_length = min(len(s) for s in strs)
        for i in range(min_length):
            next_char = strs[0][i]
            for string in strs[1:]:
                if string[i] != next_char:
                    return longest
            longest += next_char
        return longest