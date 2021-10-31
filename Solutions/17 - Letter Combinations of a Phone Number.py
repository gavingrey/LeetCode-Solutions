possibilities = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g','h','i'],
    '5': ['j','k','l'],
    '6': ['m','n','o'],
    '7': ['p','q','r','s'],
    '8': ['t','u','v'],
    '9': ['w','x','y','z'],
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits:
            ans = [""]
            temp_result = []
            for digit in digits:
                for letter in possibilities[digit]:
                    temp_result.extend(list(map(lambda number: number + letter, ans)))
                ans = temp_result
                temp_result = []
            return ans
        return []