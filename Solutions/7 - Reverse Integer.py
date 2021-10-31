class Solution:
    def reverse(self, x: int) -> int:
        neg = 1
        if x < 0:
            neg = -1
            x *= -1
        list_x = list(str(x))
        list_x.reverse()
        ans = neg * int("".join(list_x))
        return ans if (ans <= 2**31 - 1 and ans >= -2**31) else 0