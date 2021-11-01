# ()
# (()), ()()
# ((())), ()(()), (()()), ()()()

class Solution:
    def parenthesis_generator(self, existing: str, open: int, close: int):
        #Base Cases
        if open == 0 and close == 0:
            return [existing]
        elif open == 0:
            return [existing + ")" * close]
        elif open == close:
            return self.parenthesis_generator(existing = existing + "(", open = open - 1, close = close)
        else:
            possibilities = []
            possibilities.extend(self.parenthesis_generator(existing = existing + "(", open = open - 1, close = close))
            possibilities.extend(self.parenthesis_generator(existing = existing + ")", open = open, close = close - 1))
            return possibilities

    def generateParenthesis(self, n: int) -> list[str]:
        return self.parenthesis_generator(existing="", open=n, close=n)

if __name__ == '__main__':
    test = Solution()
    four_ans = test.generateParenthesis(4)
    real_ans = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
    assert not [i for i in real_ans if not i in four_ans]
