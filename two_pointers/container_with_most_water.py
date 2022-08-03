class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        result = 0
        while i < j:
            result = max(result, (j - i) * min(height[i], height[j]))
            if height[i] > height[j]:
                j -=1
            else:
                i += 1
        return result