class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ans = set()
        nums = sorted(nums)
        for idx1, num1 in enumerate(nums):
            remaining = nums[idx1 + 1:]
            for idx2, num2 in enumerate(remaining):
                start = idx2 + 1
                end = len(remaining) - 1
                while start < end:
                    sum = num1 + num2 + remaining[start] + remaining[end]
                    if sum == target:
                        ans.add((num1, num2, remaining[start], remaining[end]))
                        start += 1
                        end -= 1
                    elif sum > target:
                        end -= 1
                    else:
                        start += 1
        return [list(x) for x in ans]
    
if __name__ == '__main__':
    test = Solution()
    print(test.fourSum([1, 0, -1, 0, -2, 2], 0))