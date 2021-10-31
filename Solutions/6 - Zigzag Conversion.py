class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # r = 4:
        # 0, 6, 12       0, 6
        # 1, 5, 7, 11, 13      1, 5
        # 2, 4, 8, 10         2, 4
        # 3, 9, 15,           3
        
        # r = 5:
        # P    H    S
        # A   SI   ET
        # Y  I R  Y O
        # P L  I G  D Y
        # A    N    A
        
        #0, 8, 16
        #
        
        mod = 2 * (numRows - 1)
        if mod > 0:
            indices = []
            for row in range(numRows):
                indices.extend([idx for idx in range(len(s)) if (idx % mod == mod - row or idx % mod == row)])
            return ("".join([s[idx] for idx in indices]))
            
        else:
            return s