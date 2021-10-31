ones_dict = {
    'one': "I",
    'five': "V",
    'next_stage': "X"
}
tens_dict = {
    'one': "X",
    'five': "L",
    'next_stage': "C"
}
hundreds_dict = {
    'one': "C",
    'five': "D",
    'next_stage': "M"
}
thousands_dict = {
    'one': "M"
}

def int_to_ones(x: int, stage: dict):
    if x < 4:
        return x * stage['one']
    elif x == 4:
        return stage['one'] + stage['five']
    elif x < 9:
        return stage['five'] + (x - 5) * stage['one']
    else:
        return stage['one'] + stage['next_stage']

class Solution:
    def intToRoman(self, num: int) -> str:
        ones = num % 10
        tens = (num // 10) % 10
        hundreds = (num // 100) % 10
        thousands = (num // 1000)
        ans = ""
        ans += int_to_ones(thousands, thousands_dict) if thousands else ''
        ans += int_to_ones(hundreds, hundreds_dict) if hundreds else ''
        ans += int_to_ones(tens, tens_dict) if tens else ''
        ans += int_to_ones(ones, ones_dict) if ones else ''
        return ans