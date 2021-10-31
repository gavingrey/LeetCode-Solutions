class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums = sorted(nums)
        difference = 10000
        closest = 0
        for idx, num in enumerate(nums[:-2]):
            start = idx + 1
            end = len(nums) - 1
            while start < end:
                temp_sum = num + nums[start] + nums[end]
                temp_dif = target - temp_sum
                if abs(temp_dif) < difference:
                    difference = abs(temp_dif)
                    closest = temp_sum
                if temp_dif == 0:
                    return temp_sum
                elif temp_dif > 0:
                    start += 1
                else:
                    end -= 1
        return closest
    
if __name__ == '__main__':
    test = Solution()
    assert test.threeSumClosest([0,2,1,-3], 1) == 0