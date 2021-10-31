class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_h = 0
        start = 0
        end = len(height) - 1
        while start != end:
            height_s = height[start]
            height_e = height[end]
            distance = end - start
            area = min(height_s, height_e) * distance
            max_h = max(max_h, area)
            if height_s < height_e:
                for i in range(distance):
                    decrease_factor = (distance - 1 - i) / distance
                    start += 1
                    if height_s < decrease_factor * height[start]:
                        break
            else:
                for i in range(distance):
                    decrease_factor = (distance - 1 - i) / distance
                    end -= 1
                    if height_e < decrease_factor * height[end]:
                        break     
        return max_h