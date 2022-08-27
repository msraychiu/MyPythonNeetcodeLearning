import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = max(piles)
        min_res = max_val

        left, right = 1, max_val
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for p in piles:
                count += math.ceil(p / mid)
            if count > h:
                left = mid + 1
            else:
                min_res = mid
                right = mid - 1

        return min_res
